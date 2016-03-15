from django.db import models
from django_enumfield import enum
from django.template.defaultfilters import slugify

class run_type(enum.Enum):
    AUTOMATIC = 0
    MANUAL = 1

    labels = {
        AUTOMATIC: 'Automatic',
        MANUAL: 'Manual'
    }

class query_type(enum.Enum):
    TITLE = 0
    TILEDESCRIPTION = 1
    DESCRIPTION = 2
    ALL = 3
    OTHER = 4

    labels = {
        TITLE: 'Tile',
        TILEDESCRIPTION: 'Tile+Description',
        DESCRIPTION: 'Description',
        ALL: 'All',
        OTHER: 'Other'
    }

class feedback_type(enum.Enum):
        NONE = 0
        PSEUDO = 1
        RELEVANCE = 2
        OTHER = 3

        labels = {
            NONE: 'None',
            PSEUDO: 'Pseudo',
            RELEVANCE: 'Relevance',
            OTHER: 'Other'
        }


class Researcher(models.Model):
	name = models.CharField(max_length=128, unique=True)
	url = models.URLField(max_length=200)
    # PROFILE PICTURE
	display_name = models.CharField(max_length=128)
	organization = models.CharField(max_length=128)
	
	slug = models.SlugField()

	def save(self, *args, **kwargs):
			# Uncomment if you don't want the slug to change every time the name changes
			#if self.id is None:
					#self.slug = slugify(self.name)
			self.slug = slugify(self.name)
			super(Researcher, self).save(*args, **kwargs)

	def __unicode__(self):  #For Python 2, use __str__ on Python 3
		return self.name


class Track(models.Model):
	title = models.CharField(max_length=128, unique=True)
	track_url = models.URLField(max_length=200)
	description = models.TextField()
	genre = models.CharField(max_length=128)
	
	slug = models.SlugField()

	def save(self, *args, **kwargs):
			# Uncomment if you don't want the slug to change every time the name changes
			#if self.id is None:
					#self.slug = slugify(self.title)
			self.slug = slugify(self.title)
			super(Track, self).save(*args, **kwargs)

	def __unicode__(self):      #For Python 2, use __str__ on Python 3
		return self.title


class Task(models.Model):
	track = models.ForeignKey(Track)
	title = models.CharField(max_length=128)
	#task_url = models.FileField()
	description = models.TextField()
	year = models.DateField()
    #judgement_file = models.FileField()
	
	slug = models.SlugField()

	def save(self, *args, **kwargs):
			# Uncomment if you don't want the slug to change every time the name changes
			#if self.id is None:
					#self.slug = slugify(self.title)
			self.slug = slugify(self.title)
			super(Task, self).save(*args, **kwargs)
	

	def __unicode__(self):      #For Python 2, use __str__ on Python 3
		return self.title


class Run(models.Model):
	researcher = models.ForeignKey(Researcher)
	task = models.ForeignKey(Task)
	name = models.CharField(max_length=128)
    #result_file = models.FileField()
	description = models.TextField()
	run_type = enum.EnumField(run_type, default=run_type.AUTOMATIC)
	query_type = enum.EnumField(query_type, default=query_type.TITLE)
	feedback_type = enum.EnumField(feedback_type, default=feedback_type.NONE)
	map = models.DecimalField(max_digits=100, decimal_places=5)
	p10 = models.DecimalField(max_digits=100, decimal_places=5)
	p20 = models.DecimalField(max_digits=100, decimal_places=5)
	
	slug = models.SlugField()

	def save(self, *args, **kwargs):
			# Uncomment if you don't want the slug to change every time the name changes
			#if self.id is None:
					#self.slug = slugify(self.name)
			self.slug = slugify(self.name)
			super(Run, self).save(*args, **kwargs)

	def __unicode__(self):      #For Python 2, use __str__ on Python 3
		return self.title
