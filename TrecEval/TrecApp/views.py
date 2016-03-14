from django.shortcuts import render
from django.http import HttpResponse
from TrecApp.models import Researcher

def home(request):
    return render(request, 'trecapp/home.html')

def about(request):
    return render(request, 'trecapp/about.html')
	
def researcher(request, username):

	context_dict = {}
	
	try:
		
		context_dict["username"] = username
		
		researcher = Researcher.objects.get(display_name=username)
		
		context_dict["name"] = researcher.name
		context_dict["url"] = researcher.url
		context_dict["organization"] = researcher.organization
		
	except Researcher.DoesNotExist:
		pass

	return render(request, "TrecApp.researcher.html", context_dict)
	

def track(request,name): #might need something to usinquely identify tracks?

	context_dict = {}
	
	try:
		
		track = Track.objects.get(title=name)
		
		context_dict["title"] = name
		context_dict["url"] = track.track_url
		context_dict["description"] = track.description
		context_dict["genre"] = track.genre
		
	except Track.DoesNotExist:
		pass

	return render(request, "TrecApp.track.html", context_dict) #track.html not created yet
	
def task(request,name): #might also need unique identifier

	context_dict = {}
	
	try:
		
		task = Task.objects.get(title=name)
		
		context_dict["title"] = name
		context_dict["task"] = task.track
		context_dict["description"] = task.description
		#context_dict["url"] = task.task_url
		context_dict["year"] = task.year
		#context_dict["judgement_file"] = task.judgement_file
		
	except Task.DoesNotExist:
		pass

	return render(request, "TrecApp.task.html", context_dict) #task.html not created yet

	
def run(request,title):
	
	context_dict = {}
	
	try:
		
		context_dict["name"] = title
		
		run = Run.objects.get(name=title)
		
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
		