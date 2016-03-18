from django.shortcuts import render
from django.http import HttpResponse

from TrecApp.models import Researcher, Run, Task, Track, run_type, query_type, feedback_type

from TrecApp.forms import *
from TrecApp.valueExtractor import *
from TrecApp.models import Run, Researcher
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    runs_list = Run.objects.order_by('name')[:5]

    context_dict = {}

    #context_dict = {'runs': runs_list}

    # Render the response and send it back!
    return render(request, 'TrecApp/home.html', context_dict)

def about(request):
    return render(request, 'trecapp/about.html')



def uploadRun(request):

    currentUser = User.objects.get(username=request.user.username)      #get current user from request
    try:            #retrieve researcher for the current user from database
        researcher = Researcher.objects.get(user=currentUser)
    except Researcher.DoesNotExist:
        researcher = None

    def handle_uploaded_file(qRel,f):
        #qRel = "/Users/David/Documents/GitHub/TrecEval-WebApp/Extra/TrecEvalProgram/data/news/ap.trec.qrels"
        #qRel = "H:\Workspace\WAD\TrecWebApp\TrecEval-WebApp\Extra\TrecEvalProgram\data\news\ap.trec.qrels"
        print qRel
        results = trec_eval(qRel, f)
        return results

    if request.method == 'POST':
        form = RunForm(request.POST, request.FILES)
        if form.is_valid():
            if researcher:
                page = form.save(commit=False)
                print "Hello! Just about to call trec_eval"
                result = handle_uploaded_file(page.task.judgement_file.path,request.FILES['runfile'])
                slugFinder = page.name
                page.MAP = result['MAP']
                page.p10 = result['p10']
                page.p20 = result['p20']
                page.researcher = researcher    #foreign key
                page.save()

                #runObject = Run.objects.get(name=slugFinder)
                #slugFinder = runObject.slug
                slugFinder = Run.objects.get(name=slugFinder).slug
                return run(request, slugFinder)    #go to home page
    else:
        form = RunForm()

    return render(request, 'TrecApp/uploadRun.html',{'form': form})

def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/trecapp/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your TrecEval account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'trecapp/login.html', {})


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
        #context_dict["user"] = researcher.username

    except Researcher.DoesNotExist:
        pass

    return render(request, "TrecApp/researcher.html", context_dict)


def addResearcher(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        researcher_form = ResearcherForm(data=request.POST)

        if user_form.is_valid() and researcher_form.is_valid():
            #deals with django User model
            user = user_form.save()
            user.username = user.username.lower()

            userUsername = user.username
            userPassword = user.password
            user.set_password(user.password)
            user.save()
            #deals with our additional attributes
            researcher = researcher_form.save(commit=False)          #slug gets created by save here

            if 'picture' in request.FILES:
                researcher.picture = request.FILES['picture']

            researcher.user = user
            researcher.save()
            registered = True

            loggedinUser = authenticate(username=userUsername,password=userPassword)    #logs user in
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
    return render(request, 'TrecApp/addresearcher.html', {'user_form': user_form,'researcher_form':researcher_form, 'registered' : registered} )



def track(request,track_name_slug): #might need something to usinquely identify tracks?

    context_dict = {}
    
    
    try:
        track = Track.objects.get(slug=track_name_slug)
        tasks = Task.objects.filter(track=track)
        context_dict["track"] = track
        context_dict["tasks"] = tasks
        context_dict["title"] = track.title
        context_dict["url"] = track.track_url
        context_dict["description"] = track.description
        context_dict["genre"] = track.genre

    except Track.DoesNotExist:
        pass

    return render(request, "TrecApp/track.html", context_dict) #track.html not created yet

def trackList(request):
    context_dict = {}
    
    try:
        tracks = Track.objects.filter()
        context_dict["tracks"] = tracks


    except Track.DoesNotExist:
        pass

    return render(request, "TrecApp/tracklist.html", context_dict) #track.html not created yet
    


def task(request,track_name_slug,task_name_slug):

    context_dict = {}

    try:
        runs = Run.objects.all()
        task = Task.objects.get(slug=task_name_slug)
        context_dict["runs"] = runs
        context_dict["title"] = task.title
        context_dict["task"] = task.track
        context_dict["description"] = task.description
        #context_dict["url"] = task.task_url
        context_dict["year"] = task.year
        #context_dict["judgement_file"] = task.judgement_file

    except Task.DoesNotExist:
        pass

    return render(request, "TrecApp/task.html", context_dict) #task.html not created yet

def graph(request, run_name_slug):

    context_dict = {}

    try:

        run = Run.objects.get(slug=run_name_slug)

        context_dict["name"] = run.name
        r = run.researcher
        context_dict["researcher_name"] = r.name
        context_dict["map"] = run.MAP
        context_dict["p10"] = run.p10
        context_dict["p20"] = run.p20

        context_dict["run"] = run

    except:
        pass

    #print context_dict
    return render(request, "TrecApp/graph.html", context_dict)


def lineGraph(request, researcher_name_slug):

    context_dict = {}

    try:

        r = Researcher.objects.get(slug=researcher_name_slug)

        runs = Run.objects.filter(researcher=r).order_by("-MAP") #might need to limit amount

        context_dict["researcher"] = r

        context_dict["runs"] = runs

        print runs[0].p10

    except:
        pass

    return render(request, "TrecApp/lineGraph.html", context_dict)



def run(request,run_name_slug):

    context_dict = {}

    try:
        run = Run.objects.get(slug=run_name_slug)

        context_dict["run"] = run
        context_dict["name"] = run.name
        context_dict["researcher"] = run.researcher
        #context_dict["task"] = run.task
        #context_dict["result_file"] = run.result_file
        context_dict["map"] = run.MAP
        context_dict["description"] = run.description
        context_dict["p10"] = run.p10
        context_dict["p20"] = run.p20
        context_dict["run_type"] = run_type.labels[run.run_type]
        context_dict["feedback_type"] = feedback_type.labels[run.feedback_type]
        context_dict["query_type"] = query_type.labels[run.feedback_type]

    except Run.DoesNotExist:
        pass

    return render(request, "TrecApp/run.html", context_dict)
