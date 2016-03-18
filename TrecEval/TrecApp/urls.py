from django.conf.urls import patterns, url
from TrecApp import views

urlpatterns = patterns('',
		url(r'^$', views.home, name='home'),
		url(r'about/$', views.about, name='about'),
		url(r'^uploadrun/$', views.uploadRun, name='uploadRun'),
		url(r'run/(?P<run_name_slug>[\w\-]+)/$', views.run, name='run'),
		url(r'linegraph/(?P<researcher_name_slug>[\w\-]+)$', views.lineGraph, name='lineGraph'),
		url(r'graph/(?P<run_name_slug>[\w\-]+)$', views.graph, name='graph'),
		url(r'researcher/(?P<researcher_name_slug>[\w\-]+)/$', views.researcher, name='researcher'),
		url(r'^addresearcher/$', views.addResearcher, name='addResearcher'),
		url(r'^login/$', views.user_login, name='login'),
		url(r'^logout/$', views.user_logout, name='logout'),
		url(r'^restricted/', views.restricted, name='restricted'),
		url(r'^researcher/(?P<researcher_name_slug>[\w\-]+)/$', views.researcher, name='researcher'),
                url(r'^tracks/(?P<track_name_slug>[\w\-]+)/$', views.track, name='track'),
                url(r'^tracks/(?P<track_name_slug>[\w\-]+)/(?P<task_name_slug>[\w\-]+)/$', views.task, name='track'),
                url(r'^tracklist/$', views.trackList, name='trackList'),
                )
