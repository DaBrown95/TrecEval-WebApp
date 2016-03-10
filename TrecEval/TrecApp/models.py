from django.db import models


class Researcher(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=200)
    display_name = models.CharField(max_length=128)
    organization = models.CharField(max_length=128)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

Track (title, track_url, description, genre)

class Track(models.Model):
    title = models.CharField(max_length=128)
    track_url = model.URLField(max_length=200)
    description = models.TextField()
    genre = model.CharField(max_length=128)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title
