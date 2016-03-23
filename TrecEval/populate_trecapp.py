import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TrecEval.settings')

from datetime import datetime
from django.contrib.auth.models import User
import django

django.setup()

from TrecApp.models import Task, Track, Run, Researcher


def populate():
    joe = add_researcher("joe", "joe", "www.http://www.google.com", "google", "joe")
    jill = add_researcher("jill", "jill", "www.http://www.yahoo.com", "yahoo", "jill")
    jim = add_researcher("jim", "jim", "www.http://www.bing.com", "google", "jim")
    AlphaTeam = add_researcher("AlphaTeam", "AlphaTeam", "www.http://www.bing.com", "AS University", "ASU")
    CK = add_researcher("Chaos and Kontrol", "Chaos and Kontrol", "www.http://www.swag.com", "CK University", "CK")
    HK = add_researcher("HongKongIR", "HongKongIR", "www.http://www.sausage.com", "HK University", "HK")
    ICT = add_researcher("ICTer", "ICTer", "www.http://www.yolo.com", "University of ICT", "ICT")
    RIM = add_researcher("IRJobs", "IRJobs", "www.http://www.cool.com", "Royal Institure of Mayhem", "RIM")

    # does it matter what genre is?
    track1 = add_track("Robust", "http://trec.nist.gov/data/t14_robust.html", "News Retrieval", "News")
    track2 = add_track("APNews", "http://trec.nist.gov/tracks.html3", "news retrieval track", "News")
    track3 = add_track("Terabyte", "http://www-nlpir.nist.gov/projects/terabyte/", "Terabyte Web Track", "Web")
    #track4 = add_track("Robust2004", "http://trec.nist.gov/data/t13_robust.html", "News Retrieval", "News")
    track5 = add_track("MillionQuery", "http://ciir.cs.umass.edu/research/million/", "Million Query Track", "Web")

    # not sure if this is how to use qrels
    task1 = add_task(track1, "Robust2005,Ad Hoc Topic Retrieval", "For each topic find all the relevant documents",
                     2005, "static/Tracks/Robust2005/aq.trec2005.qrels")
    task2 = add_task(track2, "APNews,Ad Hoc Topic Retrieval", "Find all the relevant news articles", 2001,
                     "static/Tracks/news/ap.trec.qrels")
    task3 = add_task(track3, "Web2005,Ad Hoc Topic Retrieval", "Find all the relevant web pages", 2005,
                     "static/Tracks/web/dg.trec.qrels")
    task4 = add_task(track1, "Robust2004,Ad Hoc Topic Retrieval", "For each topic find all the relevant documents",
                     2004, "static/Tracks/Robust2004/qrels.robust2004.txt")

    # might have to replace some of these values with actual data
    # havent put anything in for files yet
    run1 = add_run("run1", AlphaTeam, task1, "example description", 1, 2, 3, 0.5, 0.6, 0.4)
    run2 = add_run("run2", CK, task2, "example description", 1, 3, 2, 0.6, 0.9, 0.8)
    run3 = add_run("run3", ICT, task3, "example description", 0, 2, 1, 0.2, 0.3, 0.7)
    run4 = add_run("run4", RIM, task3, "example description", 0, 1, 1, 0.4, 0.2, 0.6)
    run4 = add_run("run5", HK, task3, "example description", 1, 3, 1, 0.2, 0.1, 0.3)


def add_researcher(username, password, url, organization, name, picture=None):
    u = User.objects.get_or_create(username=username)[0]
    u.password = password
    u.save()
    r = Researcher.objects.get_or_create(user=u)[0]
    r.user = u
    r.url = url
    r.organization = organization
    r.name = name
    r.display_name = username
    # r.picture = picture
    r.save()
    return r


def add_run(name, researcher, task, description, run_type, query_type, feedback_type, MAP, p10, p20):
    r = Run.objects.get_or_create(name=name, researcher=researcher, task=task, MAP=MAP, p10=p10, p20=p20)[0]

    r.feedback_type = feedback_type
    r.run_type = run_type
    r.query_type = query_type
    r.MAP = MAP
    r.p10 = p10
    r.p20 = p20
    r.description = description
    r.researcher = researcher
    r.task = task

    r.save()

    return r


def add_track(title, url, description, genre):
    t = Track.objects.get_or_create(title=title)[0]
    t.track_url = url
    t.description = description
    t.genre = genre
    t.save()
    return t


def add_task(track, title, description, year, judgement):
    t = Task.objects.get_or_create(track=track, title=title, year=year)[0]

    t.track = track
    t.description = description
    t.year = year
    t.judgement_file = judgement

    t.save()

    return t

##<<<<<<< HEAD
##	#qrels is task
##	
##	#res is run
##	
##	joe = add_researcher("joe","joe","www.http://www.google.com","google","joe")
##	jill = add_researcher("jill","jill","www.http://www.yahoo.com","yahoo","jill")
##	jim = add_researcher("jim","jim","www.http://www.bing.com","google","jim")
##	
##	#does it matter what genre is? 
##	track1 = add_track("robust","http://trec.nist.gov/data/robust.html","first track added","robust")
##	track2 = add_track("web","http://www-personal.umich.edu/~kevynct/trec-web-2014/","second track added","web")
##	track3 = add_track("news","http://trec.nist.gov/tracks.html3","third track added","news")
##	
##	#not sure if this is how to use qrels
##	task1 = add_task(track1,"task1","description",2004,"static/Tracks/web/dg.trec.qrels")
##	task2 = add_task(track2,"task2","description",2005,"static/Tracls/Robust/aq.trec2005.qrels")
##	task3 = add_task(track3,"task3","description",2006,"static/Tracks/news/ap.trec.qrels")
##	
##	
##	#might have to replace some of these values with actual data
##	#havent put anything in for files yet
##	run1 = add_run("run1", joe, task1, "description", 1, 2, 3, 0.5, 0.6, 0.4)
##	run2 = add_run("run2", jill, task2, "description", 1, 3, 2, 0.6, 0.9, 0.8)
##	run3 = add_run("run3", jim, task3, "description", 0, 2, 1, 0.2, 0.3, 0.7)
##	run4 = add_run("run4", jim, task3, "description", 0, 2, 1, 0.4, 0.2, 0.6)
##	
##
##def add_researcher(username,password, url, organization, name, picture=None):
##        u = User.objects.get_or_create(username=username)[0]
##        u.password = password
##        u.save()
##	r = Researcher.objects.get_or_create(user=u)[0]
##	r.user = u
##	r.url=url
##	r.organization = organization
##	r.name = name
##	r.display_name = username
##	#r.picture = picture
##        r.save()
##        return r
##	
##
##
##def add_run(name, researcher, task, description, run_type, query_type, feedback_type, MAP, p10, p20):
##	
##	r = Run.objects.get_or_create(name=name,researcher=researcher,task=task,MAP=MAP,p10=p10,p20=p20)[0]
##	
##	r.feedback_type = feedback_type
##	r.run_type = run_type
##	r.query_type = query_type
##	r.MAP = MAP
##	r.p10 = p10
##	r.p20 = p20
##	r.description = description
##	r.researcher = researcher
##	r.task = task
##	
##	r.save()
##	
##        return r
##	
##def add_track(title,url,description,genre):
##	
##	t = Track.objects.get_or_create(title=title)[0]
##	t.url = url
##	t.description = description
##	t.genre = genre
##	t.save()
##	return t
##	
##def add_task(track,title,description,year,judgement):
##	
##	t = Task.objects.get_or_create(track=track,title=title,year=year)[0]
##
##	t.track = track
##	t.description = description
##	t.year = year
##	t.judgement_file = judgement
##	
##	t.save()
##	
##	return t
##=======
##>>>>>>> 9690fcd883100734f2c3861fd14177376525038a

# Start execution here!
if __name__ == '__main__':
    print "Starting TrecApp population script..."
    populate()
