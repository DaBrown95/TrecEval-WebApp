from django.conf.urls import patterns, url
from TrecApp import views

urlpatterns = patterns('',
    url(r'^$', views.uploadRun, name='index'),
    url(r'^about/$', views.uploadRun, name='about'),                  
    url(r'^uploadRun/$', views.uploadRun, name='uploadRun'),
)
