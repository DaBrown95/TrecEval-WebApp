from django.test import TestCase
from django.contrib.auth.models import User

from TrecApp.models import Researcher, Track, Run, Task
from TrecApp.forms import ResearcherForm


class ResearcherTests(TestCase):
    def setUp(self):
        self.bobUser = User.objects.create(username="Bob Bobby Brown")
        Researcher.objects.create(user=self.bobUser, url="www.gla.ac.uk", organization="Glasgow University")

    def test_slug_line_creation(self):
        bob = Researcher.objects.get(user=self.bobUser)
        self.assertEquals(bob.slug, "bob-bobby-brown")

        # def test_url_cleaner(self):
        #     bob = Researcher.objects.get(user=self.bobUser)
        #     data = {
        #         'user': bob,
        #         'url': bob.url,
        #         'display_name': bob.display_name,
        #         'organization': bob.organization
        #
        #     }
        #     form = ResearcherForm(data)
        #     self.assertFalse(form.is_valid())
        #     print form['url']
        #     #print form.clean()
        #     self.assertEquals(form['url'], "http://www.gla.ac.uk"


class TrackTests(TestCase):
    def setUp(self):
        Track.objects.create(title='Robust')

    def test_slug_line_creation(self):
        robust = Track.objects.get(title='Robust')
        self.assertEquals(robust.slug, 'robust')


class TaskTests(TestCase):
    def setUp(self):
        robust = Track.objects.create(title='Robust')
        Task.objects.create(track=robust, title='Robust2004', year=2004)

    def test_slug_line_creation(self):
        robust = Task.objects.get(title='Robust2004')
        self.assertEquals(robust.slug, 'robust2004')


class RunTests(TestCase):
    def setUp(self):
        self.bobUser = User.objects.create(username="Bob Bobby Brown")
        bob = Researcher.objects.create(user=self.bobUser, url="www.gla.ac.uk", organization="Glasgow University")
        robust = Track.objects.create(title='Robust')
        robust2004 = Task.objects.create(track=robust, title='Robust2004', year=2004)
        Run.objects.create(name='My Super Cool Run', MAP=0.0, p10=0.0, p20=0.0, researcher=bob, task=robust2004)

    def test_slug_creation(self):
        robust2004 = Run.objects.get(name='My Super Cool Run')
        self.assertEquals(robust2004.slug, 'my-super-cool-run')
