import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TrecEval.settings')

from datetime import datetime
from django.contrib.auth.models import User
import django

django.setup()

from TrecApp.models import Task, Track, Run, Researcher

from datetime import datetime
import random
import string


def populate():
    joe = add_researcher("joe", "joe", "www.http://www.google.com", "google", "joe")
    jill = add_researcher("jill", "jill", "www.http://www.yahoo.com", "yahoo", "jill")
    jim = add_researcher("jim", "jim", "www.http://www.bing.com", "google", "jim")
    AlphaTeam = add_researcher("AlphaTeam", "AlphaTeam", "www.http://www.bing.com", "AS University", "ASU")
    CK = add_researcher("Chaos and Kontrol", "Chaos and Kontrol", "www.http://www.swag.com", "CK University", "CK")
    HK = add_researcher("HongKongIR", "HongKongIR", "www.http://www.sausage.com", "HK University", "HK")
    ICT = add_researcher("ICTer", "ICTer", "www.http://www.yolo.com", "University of ICT", "ICT")
    RIM = add_researcher("IRJobs", "IRJobs", "www.http://www.cool.com", "Royal Institure of Mayhem", "RIM")
    bob = add_researcher("bob", "bob", "www.http://www.facebook.com", "Anonymous","bob")

    # does it matter what genre is?
    track1 = add_track("Robust", "http://trec.nist.gov/data/t14_robust.html", "News Retrieval", "News")
    track2 = add_track("APNews", "http://trec.nist.gov/tracks.html3", "news retrieval track", "News")
    track3 = add_track("Terabyte", "http://www-nlpir.nist.gov/projects/terabyte/", "Terabyte Web Track", "Web")
    # track4 = add_track("Robust2004", "http://trec.nist.gov/data/t13_robust.html", "News Retrieval", "News")
    track5 = add_track("MillionQuery", "http://ciir.cs.umass.edu/research/million/", "Million Query Track", "Web")
    track6 = add_track("ConfusionTrack", "http://trec.nist.gov/data/t5_confusion.html","Confusion Track","Web")

    # not sure if this is how to use qrels
    task1 = add_task(track1, "Robust2005,Ad Hoc Topic Retrieval", "For each topic find all the relevant documents",
                     2005, "Tracks/Robust2005/aq.trec2005.qrels")
    task2 = add_task(track2, "APNews,Ad Hoc Topic Retrieval", "Find all the relevant news articles", 2001,
                     "Tracks/news/ap.trec.qrels")
    task3 = add_task(track3, "Web2005,Ad Hoc Topic Retrieval", "Find all the relevant web pages", 2005,
                     "Tracks/web/dg.trec.qrels")
    task4 = add_task(track1, "Robust2004,Ad Hoc Topic Retrieval", "For each topic find all the relevant documents",
                     2004, "static/Tracks/Robust2004/qrels.robust2004.txt")
    

    # might have to replace some of these values with actual data
    # havent put anything in for files yet
    run1 = add_run("run1", AlphaTeam, task2, "example description", 1, 2, 3, 0.5, 0.6, 0.4, datetime(2000, 1, 01))
    run2 = add_run("run2", CK, task2, "example description", 1, 3, 2, 0.6, 0.9, 0.8, datetime(2005, 5, 05))
    run3 = add_run("run3", ICT, task3, "example description", 0, 2, 1, 0.2, 0.3, 0.7, datetime(2010, 10, 10))
    run4 = add_run("run4", RIM, task3, "example description", 0, 1, 1, 0.4, 0.2, 0.6, datetime(2015, 3, 15))
    run5 = add_run("run5", HK, task3, "example description", 1, 3, 1, 0.2, 0.1, 0.3, datetime.now())
    run6 = add_run("run6", joe, task4, "example description", 0, 2, 1, 0.9, 0.7, 0.4, datetime(2004,5,9))
    run7 = add_run("bobs run", bob, task4, "example description", 1, 3, 1, 0.9, 0.7, 0.8, datetime(1887,4,2))


    add_run("a",ICT,task1,"description",1,1,1,0.54,0.42,0.34,datetime(2001,2,3))
    add_run("b",jill,task1,"description",1,1,1,0.25,0.22,0.23,datetime(2011,4,9))
    add_run("c",joe,task1,"description",1,1,1,0.57,0.72,0.37,datetime(2013,1,7))
    add_run("segsgr",HK,task1,"description",1,1,1,0.51,0.21,0.13,datetime(2007,2,12))
    add_run("aaef",bob,task1,"description",1,1,1,0.58,0.82,0.83,datetime(2014,1,2))
    add_run("aseg",bob,task1,"description",1,1,1,0.53,0.23,0.33,datetime(2010,2,2))
    add_run("arsg",bob,task1,"description",1,1,1,0.75,0.27,0.73,datetime(2004,8,4))
    add_run("asgefse",bob,task1,"description",1,1,1,0.75,0.12,0.3,datetime(2034,6,1))
    


def name_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


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


def add_run(name, researcher, task, description, run_type, query_type, feedback_type, MAP, p10, p20, date):
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
    r.date = date
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


##
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
##	task1 = add_task(track1,"task1","description",2004,"Tracks/web/dg.trec.qrels")
##	task2 = add_task(track2,"task2","description",2005,"Tracls/Robust/aq.trec2005.qrels")
##	task3 = add_task(track3,"task3","description",2006,"Tracks/news/ap.trec.qrels")
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

# Start execution here!
if __name__ == '__main__':
    print "Starting TrecApp population script..."
    populate()
