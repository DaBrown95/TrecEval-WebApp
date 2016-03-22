from django.conf.urls import patterns, url
from TrecApp import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'about/$', views.about, name='about'),
                       url(r'tasks/$', views.tasks, name='tasks'),
                       url(r'tasks/(?P<task_name_slug>[\w\-]+)/$', views.task, name='task'),
                       url(r'tracks/$', views.tracks, name='tracks'),
                       url(r'tracks/(?P<track_name_slug>[\w\-]+)/$', views.track, name='track'),
                       url(r'^uploadrun/$', views.uploadRun, name='uploadRun'),
                       url(r'run/(?P<run_name_slug>[\w\-]+)/$', views.run, name='run'),
                       url(r'lineGraph/$', views.lineGraph, name='lineGraph'),
                       url(r'compareRuns/$', views.compareRuns, name='compareRuns'),
                       url(r'graph/(?P<run_name_slug>[\w\-]+)$', views.graph, name='graph'),
                       url(r'researcher/(?P<researcher_name_slug>[\w\-]+)/$', views.researcher, name='researcher'),
                       url(r'^addresearcher/$', views.addResearcher, name='addResearcher'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^restricted/', views.restricted, name='restricted'),
                       url(r'^researchers/', views.researchers, name='researcher'),
                       url(r'^researcher/(?P<researcher_name_slug>[\w\-]+)/$', views.researcher, name='researcher'),
                       url(r'^updateprofile/$', views.update_profile, name='updateprofile'),
                       url(r'^termsandconditions/$', views.terms, name='terms'), )
