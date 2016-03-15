import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TrecEval.settings')

import django
django.setup()

from rango.models import Task, Track, Run, Researcher

def populate():
	
	## add population data here

def add_researcher(username, url, organization, name, picture=None):
	r = Researcher.objects.get_or_create()[0]
	r.url=url
	r.organization = organization
	r.name = name
	r.display_name = username
	#r.picture = picture
    r.save()
    return r
	


def add_run(name, researcher, task, description, run_type, query_type, feedback_type, map, p10, p20):
	r = Run.objects.get_or_create(name=name)[0]
	
	r.feedback_type = feedback_type
	r.run_type = run_type
	r.query_type = query_type
	r.map = map
	r.p10 = p10
	r.p20 = p20
	r.description = description
	r.researcher = researcher
	r.task = task
	
	r.save()
	
    return r
	
def add_track(title,url,description,genre):
	
	t = Track.objects.get_or_create(title=title)[0]
	
	t.url = url
	t.description = description
	t.genre = genre
	
	t.save()
	
	return task
	
def add_task(track,title,description,year):
	
	t = Task.objects.get_or_create(title=title)[0]
	
	
	t.track = track
	t.description = description
	t.year = year
	
	t.save()
	
	return t

# Start execution here!
if __name__ == '__main__':
    print "Starting TrecApp population script..."
    populate()