from django.shortcuts import render
from django.http import HttpResponse
from TrecApp.forms import RunForm
from TrecApp.models import Run
from TrecApp.valueExtractor import *

def home(request):
    return render(request, 'trecapp/home.html')

def about(request):
    return render(request, 'trecapp/about.html')

def uploadRun(request):

    def handle_uploaded_file(f):
        qRel = "/Users/David/Documents/GitHub/TrecEval-WebApp/Extra/TrecEvalProgram/data/news/ap.trec.qrels"
        results = trec_eval(qRel, f)
        return results

    if request.method == 'POST':
        form = RunForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            result = handle_uploaded_file(request.FILES['runfile'])
            page.MAP = result['MAP']
            page.p10 = result['p10']
            page.p20 = result['p20']
            page.save()
            return home(request)    #go to home page
    else:
        form = RunForm()

    return render(request,'TrecApp/uploadRun.html',{'form': form})
