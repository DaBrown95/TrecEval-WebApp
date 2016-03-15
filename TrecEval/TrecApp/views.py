from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'trecapp/home.html')

def about(request):
    return render(request, 'trecapp/about.html')
