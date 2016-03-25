import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TrecEval.settings')

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from faker import Factory
import django

django.setup()

from TrecApp.models import Task, Track, Run, Researcher

import random


def populate():
    track1 = add_track("Robust2005", "http://trec.nist.gov/data/t14_robust.html", "News Retrieval", "News")
    track2 = add_track("APNews", "http://trec.nist.gov/tracks.html3", "news retrieval track", "News")
    track3 = add_track("Terabyte", "http://www-nlpir.nist.gov/projects/terabyte/", "Terabyte Web Track", "Web")
    track4 = add_track("Robust2004", "http://trec.nist.gov/data/t13_robust.html", "News Retrieval", "News")
    track5 = add_track("MillionQuery", "http://ciir.cs.umass.edu/research/million/", "Million Query Track", "Web")
    track6 = add_track("ConfusionTrack", "http://trec.nist.gov/data/t5_confusion.html", "Confusion Track", "Web")
    track7 = add_track("Blog2006", "http://trec.nist.gov/data/blog06.html", "Blog", "Blog")
    track8 = add_track("Blog2007", "http://trec.nist.gov/data/blog07.html", "Blog", "Blog")
    track9 = add_track("Blog2008", "http://trec.nist.gov/data/blog08.html", "Blog", "Blog")
    track10 = add_track("Blog2009", "http://trec.nist.gov/data/blog09.html", "Blog", "Blog")
    track11 = add_track("Blog2010", "http://trec.nist.gov/data/blog10.html", "Blog", "Blog")

    taskList = []
    # not sure if this is how to use qrels
    taskList.append(add_task(track1, "Ad Hoc Topic Retrieval - 2005", "For each topic find all the relevant documents",
                             2005, "Tracks/robust/2005/aq.trec2005.qrels"))
    taskList.append(add_task(track2, "APNews,Ad Hoc Topic Retrieval", "Find all the relevant news articles", 2001,
                             "Tracks/news/ap.trec.qrels"))
    taskList.append(add_task(track3, "Web2005,Ad Hoc Topic Retrieval", "Find all the relevant web pages", 2005,
                             "Tracks/web/dg.trec.qrels"))
    taskList.append(add_task(track4, "Ad Hoc Topic Retrieval - 2004", "For each topic find all the relevant documents",
                             2004, "Tracks/robust/2004/qrels.robust2004.txt"))
    taskList.append(add_task(track7, "Blogs - 2006", "For each topic find all the relevant documents", 2006,
                             "Tracks/blog/2006/qrels.blog06"))
    taskList.append(add_task(track8, "Opinions", "For each topic find all the relevant documents", 2007,
                             "Tracks/blog/2007/07.qrels.opinion"))
    taskList.append(add_task(track8, "Distillation", "For each topic find all the relevant documents", 2007,
                             "Tracks/blog/2007/07.blog.feeddist.qrels"))
    taskList.append(add_task(track9, "Opinion", "For each topic find all the relevant documents", 2008,
                             "Tracks/blog/2008/08.blog.blogdist.qrels"))
    taskList.append(add_task(track9, "Positive Polarity", "For each topic find all the relevant documents", 2008,
                             "Tracks/blog/2008/08.qrels.positive.all-topics"))
    taskList.append(add_task(track9, "Negative Polarity", "For each topic find all the relevant documents", 2008,
                             "Tracks/blog/2008/08.qrels.negative.all-topics"))
    taskList.append(
        add_task(track10, "Distillation - All Topics", "For each topic find all the relevant documents", 2009,
                 "Tracks/blog/2009/09.distillation-qrels.full"))
    taskList.append(
        add_task(track10, "Distillation - Offical Topics", "For each topic find all the relevant documents", 2009,
                 "Tracks/blog/2009/09.distillation-qrels.official"))
    taskList.append(add_task(track11, "Top Stories", "For each topic find all the relevant documents", 2010,
                             "Tracks/blog/2010/10.top-stories.blog.qrels"))

    fake = Factory.create()
    for i in range(0, 500):
        name = fake.name()
        tempRes = add_researcher(name, name, fake.url(), fake.company(), name)
        try:
            for x in range(0, fake.random_int(min=5, max=10)):
                add_run(fake.sentence(nb_words=4, variable_nb_words=True), tempRes,
                        taskList[fake.random_int(min=1, max=12)], fake.sentence(nb_words=4, variable_nb_words=True),
                        fake.random_element(elements=(0, 1)),
                        fake.random_element(elements=(0, 1, 2, 3, 4)), fake.random_element(elements=(0, 1, 2, 3)),
                        random.uniform(0, 1),
                        random.uniform(0, 1), random.uniform(0, 1), fake.date(pattern="%Y-%m-%d"))
        except IntegrityError:
            break

    usersForSubmission = []
    usersForSubmission.append(add_researcher("jill", "jill", fake.url(), fake.company(), "jill"))
    usersForSubmission.append(add_researcher("bob", "bob", fake.url(), fake.company(), "bob"))
    usersForSubmission.append(add_researcher("jen", "jen", fake.url(), fake.company(), "jen"))
    for x in range(0, 5):
        try:
            add_run(fake.sentence(nb_words=4, variable_nb_words=True), usersForSubmission[fake.random_int(min=0, max=2)],
                    taskList[fake.random_int(min=1, max=12)],
                    fake.sentence(nb_words=4, variable_nb_words=True), fake.random_element(elements=(0, 1)),
                    fake.random_element(elements=(0, 1, 2, 3, 4)), fake.random_element(elements=(0, 1, 2, 3)),
                    random.uniform(0, 1),
                    random.uniform(0, 1), random.uniform(0, 1), fake.date(pattern="%Y-%m-%d"))
        except IntegrityError:
            break

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
    #r.picture = picture
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


# Start execution here!
if __name__ == '__main__':
    print "Starting TrecApp population script..."
    populate()
