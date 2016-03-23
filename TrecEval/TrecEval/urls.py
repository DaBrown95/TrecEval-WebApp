from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^trecapp/', include('TrecApp.urls')),
                       url(r'^/?$', include('TrecApp.urls')),

                       )

if settings.DEBUG:
     urlpatterns += patterns(
         'django.views.static',
         (r'^media/(?P<path>.*)',
          'serve',
          {'document_root': settings.MEDIA_ROOT}), )
