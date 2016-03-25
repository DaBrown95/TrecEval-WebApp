import os

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

from TrecApp.models import Researcher, Track, Run, Task
from TrecApp.valueExtractor import trec_eval
from TrecEval.settings import STATIC_PATH


class ResearcherTests(TestCase):
    def setUp(self):
        self.bobUser = User.objects.create(username="Bob Bobby Brown")
        self.jillUser = User.objects.create(username="Jill Jack")
        Researcher.objects.create(user=self.bobUser, url="www.gla.ac.uk", organization="Glasgow University")

    def test_slug_line_creation(self):
        bob = Researcher.objects.get(user=self.bobUser)
        self.assertEquals(bob.slug, "bob-bobby-brown")

    def test_unique_user(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(username="Bob Bobby Brown")

    def test_unique_researcher(self):
        with self.assertRaises(IntegrityError):
            Researcher.objects.create(user=self.bobUser, url='www.apple.com')


class TrackTests(TestCase):
    def setUp(self):
        Track.objects.create(title='robust')

    def test_slug_line_creation(self):
        robust = Track.objects.get(title='robust')
        self.assertEquals(robust.slug, 'robust')


class TaskTests(TestCase):
    def setUp(self):
        robust = Track.objects.create(title='robust')
        Task.objects.create(track=robust, title='Robust2004', year=2004)

    def test_slug_line_creation(self):
        robust = Task.objects.get(title='Robust2004')
        self.assertEquals(robust.slug, 'robust2004')


class RunTests(TestCase):
    def setUp(self):
        self.bobUser = User.objects.create(username="Bob Bobby Brown")
        bob = Researcher.objects.create(user=self.bobUser, url="www.gla.ac.uk", organization="Glasgow University")
        robust = Track.objects.create(title='robust')
        robust2004 = Task.objects.create(track=robust, title='Robust2004', year=2004)
        Run.objects.create(name='My Super Cool Run', MAP=0.0, p10=0.0, p20=0.0, researcher=bob, task=robust2004)

    def test_slug_creation(self):
        robust2004 = Run.objects.get(name='My Super Cool Run')
        self.assertEquals(robust2004.slug, 'my-super-cool-run')


class ValueExtractorTests(TestCase):
    def setUp(self):
        self.filePathQREL = os.path.join(STATIC_PATH, 'TEST_FILES/ap.trec.qrels')
        self.filePathRES = os.path.join(STATIC_PATH, 'TEST_FILES/ap.trec.pl2.2.00.res')


    def test_trec_eval_works(self):
        self.assertIsNotNone(trec_eval(self.filePathQREL, self.filePathRES, True))

