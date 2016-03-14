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
	
