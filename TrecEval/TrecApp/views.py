from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
<<<<<<< HEAD
from TrecApp.models import Researcher
=======
from TrecApp.forms import RunForm
from TrecApp.models import Run
>>>>>>> master
=======
from TrecApp.forms import RunForm
from TrecApp.models import Run, Researcher
>>>>>>> master

def home(request):
    return render(request, 'trecapp/home.html')

def about(request):
    return render(request, 'trecapp/about.html')
<<<<<<< HEAD
<<<<<<< HEAD
=======


def uploadRun(request):
    if request.method == 'POST':
        form = RunForm(request.POST,request.FILES)
        if form.is_valid():
            newRunFile = Run(runfile = request.FILES['runfile'])      #no files added to context_dict yet
            newRunFile.save()
            return home(request)    #go to home page
    else:
        form = RunForm()

    return render(request,'TrecApp/uploadRun.html',{'form': form})
>>>>>>> master
	
def researcher(request, researcher_name_slug):

	context_dict = {}
	
	try:
		
		researcher = Researcher.objects.get(slug=researcher_name_slug)
		
		context_dict["username"] = researcher.display_name
		context_dict["name"] = researcher.name
		context_dict["url"] = researcher.url
		context_dict["organization"] = researcher.organization
		
	except Researcher.DoesNotExist:
		pass

	return render(request, "TrecApp.researcher.html", context_dict)
	

def track(request,track_name_slug): #might need something to usinquely identify tracks?

	context_dict = {}
	
	try:
		
		track = Track.objects.get(slug=track_name_slug)
		
		context_dict["title"] = track.title
		context_dict["url"] = track.track_url
		context_dict["description"] = track.description
		context_dict["genre"] = track.genre
		
	except Track.DoesNotExist:
		pass

	return render(request, "TrecApp.track.html", context_dict) #track.html not created yet
	
def task(request,task_name_slug):

	context_dict = {}
	
	try:
		
		task = Task.objects.get(slug=task_name_slug)
		
		context_dict["title"] = task.title
		context_dict["task"] = task.track
		context_dict["description"] = task.description
		#context_dict["url"] = task.task_url
		context_dict["year"] = task.year
		#context_dict["judgement_file"] = task.judgement_file
		
	except Task.DoesNotExist:
		pass

	return render(request, "TrecApp.task.html", context_dict) #task.html not created yet

def graph(request, run_name_slug):

	context_dict = {}
	
	try:
		run = Run.objects.get(slug=run_name_slug)
		context_dict["name"] = run.name
		context_dict["map"] = run.Map
		context_dict["p10"] = run.p10
		context_dict["p20"] = run.p20
	
	except:
		pass

	return render(request, TrecApp.graph.html, context_dict)

	
	
	
def run(request,run_name_slug):
	
	context_dict = {}
	
	try:
			
		run = Run.objects.get(slug=run_name_slug)
		
		context_dict["name"] = run.name
		context_dict["researcher"] = run.researcher
		context_dict["task"] = run.task
		#context_dict["result_file"] = run.result_file
		context_dict["map"] = run.Map
		context_dict["description"] = run.description
		context_dict["p10"] = run.p10
		context_dict["p20"] = run.p20
		context_dict["run_type"] = run.run_type
		context_dict["feedback_type"] = run.feedback_type
		context_dict["query_type"] = run.query_type
		
	except Run.DoesNotExist:
		pass
		
	return render(request, TrecApp.run.html, context_dict)
<<<<<<< HEAD
		
=======

def uploadRun(request):
    if request.method == 'POST':
        form = RunForm(request.POST,request.FILES)
        if form.is_valid():
            newRunFile = Run(runfile = request.FILES['runfile'])      #no files added to context_dict yet
            newRunFile.save()
            return home(request)    #go to home page
    else:
        form = RunForm()

    return render(request,'TrecApp/uploadRun.html',{'form': form})
>>>>>>> master
=======
>>>>>>> master
