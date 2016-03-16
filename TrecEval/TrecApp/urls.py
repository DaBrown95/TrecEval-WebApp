from django.conf.urls import patterns, url
from TrecApp import views

urlpatterns = patterns('',
<<<<<<< HEAD
        url(r'^$', views.home, name='home'),
        url(r'about/$', views.about, name='about'),
<<<<<<< HEAD
=======
		url(r'^$', views.home, name='home'),
		url(r'about/$', views.about, name='about'),
		url(r'^uploadrun/$', views.uploadRun, name='uploadRun'))
>>>>>>> master
		url(r'run/(?P<run_name_slug>[\w\-]+)/$', views.run, name='run'),
		url(r'run/graph/$', views.graph, name='graph'),
		url(r'researcher/(?P<researcher_name_slug>[\w\-]+)/$', views.researcher, name='researcher')
		)
<<<<<<< HEAD
=======
        url(r'^uploadrun/$', views.uploadRun, name='uploadRun'))
>>>>>>> master
=======
>>>>>>> master
