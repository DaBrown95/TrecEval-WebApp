from django.shortcuts import render
from django.http import HttpResponse

from TrecApp.models import Researcher, Run, Task, Track, run_type, query_type, feedback_type

from TrecApp.forms import *
from TrecApp.valueExtractor import *
from TrecApp.models import Run, Researcher
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from TrecApp.tables import RunTable, TaskTable, ResearcherTable
from django_tables2 import RequestConfig
import simplejson


def home(request):
    runs_list = Run.objects.order_by('-date')[:5]

    context_dict = {}

    context_dict = {'runs': runs_list}

    # Render the response and send it back!
    return render(request, 'TrecApp/home.html', context_dict)


def researchers(request):
    context_dict = {}

    allResearchers = Researcher.objects.order_by("display_name")
    #context_dict["researchers"] = researchers_list
    researcherList = []
    for researcherCursor in allResearchers:
        researcherDict = {}
        researcherDict['display_name'] = researcherCursor.display_name
        researcherDict['organization'] = researcherCursor.organization
        researcherDict['slug'] = researcherCursor.slug
        researcherDict['numberOfRuns'] = Run.objects.filter(researcher=researcherCursor).count()
        researcherList += [researcherDict]

    table = ResearcherTable(researcherList)
    RequestConfig(request,paginate={"per_page": 10}).configure(table)
    context_dict["table"] = table

    return render(request, "TrecApp/researchers.html", context_dict)


def about(request):
    return render(request, 'TrecApp/about.html')


@login_required
def uploadRun(request, task_name_slug):
    currentUser = User.objects.get(username=request.user.username)  # get current user from request
    try:  # retrieve researcher for the current user from database
        researcher = Researcher.objects.get(user=currentUser)
        task = Task.objects.get(slug=task_name_slug)
    except Researcher.DoesNotExist:
        researcher = None
        task = None
    
    def handle_uploaded_file(qRel, f):
        # qRel = "/Users/David/Documents/GitHub/TrecEval-WebApp/Extra/TrecEvalProgram/data/news/ap.trec.qrels"
        # qRel = "H:\Workspace\WAD\TrecWebApp\TrecEval-WebApp\Extra\TrecEvalProgram\data\news\ap.trec.qrels"
        results = trec_eval(qRel, f)
        return results

    if request.method == 'POST':
        form = RunForm(request.POST, request.FILES)
        
        if form.is_valid():
            if researcher:
                page = form.save(commit=False)
                page.task = task
                print "Hello! Just about to call trec_eval"
                result = handle_uploaded_file(page.task.judgement_file.path, request.FILES['runfile'])
                slugFinder = page.name
                page.MAP = result['MAP']
                page.p10 = result['p10']
                page.p20 = result['p20']
                page.researcher = researcher  # foreign key
                page.save()

                # runObject = Run.objects.get(name=slugFinder)
                # slugFinder = runObject.slug
                slugFinder = Run.objects.get(name=slugFinder).slug
                return run(request, slugFinder)  # go to home page
    else:
        form = RunForm()
        

    return render(request, 'TrecApp/uploadRun.html', {'form': form, 'task':task})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/trecapp/')
            else:
                return HttpResponse("Your TrecEval account is disabled.")
        else:
            return render(request, 'TrecApp/login.html', {})

    else:
        return render(request, 'TrecApp/login.html', {})


def restricted(request):
    return HttpResponse("Since you're logged in, you can see this!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/trecapp/')


def researcher(request, researcher_name_slug):
    context_dict = {}

    try:
        researcher = Researcher.objects.get(slug=researcher_name_slug)
        context_dict["display_name"] = researcher.display_name
        context_dict["url"] = researcher.url
        context_dict["organization"] = researcher.organization
        context_dict["runs"] = Run.objects.filter(researcher=researcher).order_by("MAP")
        context_dict["picture"] = researcher.picture
        context_dict["displayChangeProfile"] = (request.user == researcher.user)
        if researcher.picture == "":
            context_dict["hasPicture"] = False
        else:
            context_dict["hasPicture"] = True
    except Researcher.DoesNotExist:
        pass

    return render(request, "TrecApp/researcher.html", context_dict)


def addResearcher(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        researcher_form = ResearcherForm(data=request.POST)
        if user_form.is_valid() and researcher_form.is_valid():
            # deals with django User model
            user = user_form.save()
            user.username = user.username.lower()

            userUsername = user.username
            userPassword = user.password
            user.set_password(user.password)
            user.save()
            # deals with our additional attributes
            researcher = researcher_form.save(commit=False)  # slug gets created by save here

            if 'picture' in request.FILES:
                researcher.picture = request.FILES['picture']

            researcher.user = user
            researcher.save()
            registered = True

            loggedinUser = authenticate(username=userUsername, password=userPassword)  # logs user in
            if loggedinUser.is_active:
                login(request, loggedinUser)
                return home(request)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your TrecEval account is disabled.")
        else:
            # The supplied forms contained errors - just print them to the terminal.
            print user_form.errors, researcher_form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        user_form = UserForm()
        researcher_form = ResearcherForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'TrecApp/addresearcher.html',
                  {'user_form': user_form, 'researcher_form': researcher_form, 'registered': registered})


def update_profile(request):
    if request.method == 'POST':

        # form = UpdateResearcherForm(request.POST, instance=request.user)
        # form.actual_user = request.user
        form = UpdateResearcherForm(request.POST)

        if form.is_valid():
            page = form.save(commit=False)
            userProfile = Researcher.objects.get(user=request.user)
            if page.display_name != '':
                userProfile.display_name = page.display_name
            if page.url != '':
                userProfile.url = page.url
            if page.organization != '':
                userProfile.organization = page.organization
            if 'picture' in request.FILES:
                userProfile.picture = request.FILES['picture']

            userProfileSlug = userProfile.slug
            userProfile.save()
            return researcher(request, userProfileSlug)
    else:
        researcher_update_form = UpdateResearcherForm()

    return render(request, 'TrecApp/updateprofile.html', {'researcher_update_form': researcher_update_form})


def track(request, track_name_slug):
    context_dict = {}

    try:
        track = Track.objects.get(slug=track_name_slug)
        context_dict["track"] = track
        context_dict["title"] = track.title
        context_dict["url"] = track.track_url
        context_dict["description"] = track.description
        context_dict["genre"] = track.genre
        # context_dict["tasks"] = tasksFromTrack

        tasksFromTrack = Task.objects.filter(track=track)
        context_dict["tasks"] = tasksFromTrack
        taskList = []
        for taskCursor in tasksFromTrack:
            taskDict = {}
            taskDict['title'] = taskCursor.title
            taskDict['year'] = taskCursor.year
            taskDict['number'] = Run.objects.filter(task=taskCursor).count()
            taskDict['slug'] = taskCursor.slug
            taskList += [taskDict]

        table = TaskTable(taskList)
        RequestConfig(request, paginate={"per_page": 5}).configure(table)
        context_dict["table"] = table
        context_dict["number"] = tasksFromTrack.count()

    except Track.DoesNotExist:
        pass

    return render(request, "TrecApp/track.html", context_dict)


def tracks(request):
    context_dict = {}
    try:

        tracks = Track.objects.order_by("title")

        context_dict["tracks"] = tracks

    except Track.DoesNotExist:
        pass

    return render(request, "TrecApp/tracks.html", context_dict)


def tasks(request):
    context_dict = {}

    try:

        tasks = Task.objects.order_by("title")
        context_dict["tasks"] = tasks

    except Task.DoesNotExist:
        pass

    return render(request, "TrecApp/tasks.html", context_dict)


def task(request, task_name_slug):
    context_dict = {}

    try:
        task = Task.objects.get(slug=task_name_slug)


        runs = Run.objects.filter(task=task)
        bestRuns = Run.objects.filter(task=task).order_by('-MAP')[:3]

        runList = []
        for run in runs:  # creates dictionary for the table. This is needed to include the organization.
            runDict = {}
            runDict['name'] = run.name
            runDict['researcher'] = run.researcher
            runDict['task'] = run.task
            runDict['runfile'] = run.runfile
            runDict['description'] = run.description
            runDict['run_type'] = run.run_type
            runDict['query_type'] = run.query_type
            runDict['feedback_type'] = run.feedback_type
            runDict['MAP'] = run.MAP
            runDict['p10'] = run.p10
            runDict['p20'] = run.p20
            runDict['organization'] = run.researcher.organization
            runDict['date'] = run.date
            runDict['checkBox'] = run.name
            runDict['slug'] = run.slug
            runList += [runDict]

        table = RunTable(runList)
        RequestConfig(request, paginate={"per_page": 10}).configure(table)
        table.exclude = ('runfile', 'slug',)
        table.paginate
        context_dict["runs"] = runs
        context_dict["task"] = task
        context_dict["table"] = table
        context_dict["title"] = task.title
        context_dict["track"] = task.track
        context_dict["track"] = task.track
        context_dict["description"] = task.description
        context_dict["url"] = task.task_url
        context_dict["year"] = task.year

    
        if request.method == 'POST':
            dataToPass = []
            checkedRuns = request.POST.getlist('checkBox')
            
            for run in checkedRuns:
                thisRun = Run.objects.get(name=run)
                thisRun = [thisRun.name,thisRun.MAP,thisRun.p10,thisRun.p20]
                dataToPass += [thisRun]
            return lineGraph(request,dataToPass,task)
        
        
    except Task.DoesNotExist:
        pass

    return render(request, "TrecApp/task.html", context_dict)  # task.html not created yet



def graph(request, run_name_slug):
    context_dict = {}

    try:
        run = Run.objects.get(slug=run_name_slug)

        context_dict["name"] = run.name
        r = run.researcher
        context_dict["researcher_name"] = r.display_name
        context_dict["map"] = run.MAP
        context_dict["p10"] = run.p10
        context_dict["p20"] = run.p20
        context_dict["run"] = run

    except:
        pass

    # print context_dict
    return render(request, "TrecApp/graph.html", context_dict)


def lineGraph(request, runs, name):
    context_dict = {}

    try:

        json_list = simplejson.dumps(runs)

        context_dict["runs"] = json_list

        context_dict["name"] = name
 

    except:
        pass

    return render(request, "TrecApp/lineGraph.html", context_dict)


def run(request, run_name_slug):
    context_dict = {}

    try:
        run = Run.objects.get(slug=run_name_slug)

        context_dict["run"] = run
        context_dict["name"] = run.name
        context_dict["researcher"] = run.researcher
        # context_dict["task"] = run.task
        # context_dict["result_file"] = run.result_file
        context_dict["map"] = run.MAP
        context_dict["description"] = run.description
        context_dict["p10"] = run.p10
        context_dict["p20"] = run.p20
        context_dict["run_type"] = run_type.labels[run.run_type]
        context_dict["feedback_type"] = feedback_type.labels[run.feedback_type]
        context_dict["query_type"] = query_type.labels[run.feedback_type]
        context_dict["task"] = run.task
        context_dict["date"] = run.date

    except Run.DoesNotExist:
        pass

    return render(request, "TrecApp/run.html", context_dict)


def compareRuns(request):
    if request.method == 'POST':
        form = CompareForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            run1 = form.cleaned_data["run1"]
            run2 = form.cleaned_data["run2"]

            data = [run1,run2]

            runs = []
            for run in data:
                temp = [run.name,run.MAP,run.p10,run.p20]
                runs += [temp]

            print "Hello! Just about to generate graph"

            return lineGraph(request, runs, name)  # generate graph
    else:
        form = CompareForm()

    return render(request, 'TrecApp/compareRuns.html', {'form': form})


def terms(request):
    return render(request, 'TrecApp/termsandconditions.html')

def timeGraph(request, task_name_slug):
    context_dict = {}
    
    try:

        task = Task.objects.filter(slug=task_name_slug)
        
        runs = Run.objects.filter(task=task).order_by('date')

        data = []
        for run in runs:
            data += [ [str(run.date),run.MAP,run.p10,run.p20] ]
        
        json_list = simplejson.dumps(data)
        
        context_dict["runs"] = json_list

        context_dict["task"] = task
 
    except:
        print "error"

    print context_dict

    return render(request, "TrecApp/timeGraph.html", context_dict)
