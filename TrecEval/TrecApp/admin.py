from django.contrib import admin
from TrecApp.models import Researcher, Track, Task, Run

# Register your models here.
admin.site.register(Researcher)
admin.site.register(Track)
admin.site.register(Task)
admin.site.register(Run)
