from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from registration.backends.simple.views import RegistrationView
=======
from django.conf import settings
>>>>>>> master

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/trecapp/'
        
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^trecapp/', include('TrecApp.urls')),
    url(r'^$', views.home, name='home'),
    url(r'about/$', views.about, name='about'),
<<<<<<< HEAD
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/$', include('registration.backends.simple.urls')),
)
=======
    )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
>>>>>>> master
