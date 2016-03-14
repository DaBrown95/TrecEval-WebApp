from django.conf.urls import patterns, url
from TrecApp import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'about/$', views.about, name='about'),
		url(r'researcher/$', views.researcher, name='researcher')
		)
