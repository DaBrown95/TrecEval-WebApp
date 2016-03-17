from django.conf.urls import patterns, url
from TrecApp import views

urlpatterns = patterns('',
		url(r'^$', views.home, name='home'),
		url(r'about/$', views.about, name='about'),
		url(r'^uploadrun/$', views.uploadRun, name='uploadRun'),
		url(r'run/(?P<run_name_slug>[\w\-]+)/$', views.run, name='run'),
		url(r'linegraph/(?P<researcher_name_slug>[\w\-]+)$', views.lineGraph, name='lineGraph'),
		url(r'graph/(?P<run_name_slug>[\w\-]+)$', views.graph, name='graph'),
		url(r'researcher/(?P<researcher_name_slug>[\w\-]+)/$', views.researcher, name='researcher')
		)
