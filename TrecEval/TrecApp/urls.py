from django.conf.urls import patterns, url
from TrecApp import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'))
