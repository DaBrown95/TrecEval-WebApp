from django.conf.urls import patterns, url
from TrecApp import views

urlpatterns = patterns('',
		url(r'^$', views.home, name='home'),
		url(r'about/$', views.about, name='about'),
		url(r'^uploadrun/$', views.uploadRun, name='uploadRun'),
        url(r'^addresearcher/$', views.addResearcher, name='addResearcher'),
		url(r'^login/$', views.user_login, name='login'),)
