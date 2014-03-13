from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Speaker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #event = models.ForeignKey(Event, related_name='speakers')
    email = models.CharField(max_length=100, blank=True)
    profile_image = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    biography = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.first_name + self.last_name


class Session(models.Model):
    title = models.CharField(max_length=250)
    abstract = models.CharField(max_length=500)
    level = models.CharField(max_length=25, choices = ['Beginner', 'Intermediate', 'Advanced', 'All'])
    keywords = models.CharField(max_length=250, blank=True)
    speaker = models.ForeignKey(Speaker, related_name="sessions")
    event = models.ForeignKey(Event, related_name="sessions")

    def __unicode__(self):
        return self.title

