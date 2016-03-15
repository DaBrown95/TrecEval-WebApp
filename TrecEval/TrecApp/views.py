from django.shortcuts import render
from django.http import HttpResponse

from TrecApp.forms import RunForm
from TrecApp.models import Run
from TrecApp.forms import RunForm

def home(request):
    return render(request, 'trecapp/home.html')

def about(request):
    return render(request, 'trecapp/about.html')

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
