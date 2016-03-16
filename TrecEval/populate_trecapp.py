import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TrecEval.settings')

from datetime import datetime

import django
django.setup()

from rango.models import Task, Track, Run, Researcher

def populate():

	#qrels is task
	
	#res is run
	
	joe = add_researcher("joe","www.http://www.google.com","google","joe")
	jill = add_researcher("jill","www.http://www.yahoo.com","yahoo","jill")
	jim = add_researcher("jim","www.http://www.bing.com","google","jim")
	
	#does it matter what genre is? 
	track1 = add_track("track1","trecapp/track1","first track added","genre")
	track2 = add_track("track2","trecapp/track2","second track added","genre")
	track3 = add_track("track3","trecapp/track3","third track added","genre")
	
	task1 = add_task(track1,"task1","description",datetime.now(),"data/web/dg.trec.qrels")
	task2 = add_task(track2,"task2","description",datetime.now(),"data/robust/aq.trec2005.qrels")
	task3 = add_task(track3,"task3","description",datetime.now(),"data/news/ap.trec.qrels")
	
	#still to add runs
	

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
	
def add_task(track,title,description,year,judgement):
	
	t = Task.objects.get_or_create(title=title)[0]

	t.track = track
	t.description = description
	t.year = year
	t.judegement_file = judgement
	
	t.save()
	
	return t

# Start execution here!
if __name__ == '__main__':
    print "Starting TrecApp population script..."
    populate()