from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Speaker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    event = models.ForeignKey(Event, related_name='speakers')

    def __unicode__(self):
        return self.first_name + self.last_name


class Session(models.Model):
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=500)
    speaker = models.ForeignKey(Speaker, related_name="sessions")

    def __unicode__(self):
        return self.title

