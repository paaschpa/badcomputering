from django.conf.urls import *
from codecamp import views
from codecamp.api import SpeakerResource

speaker_resource = SpeakerResource()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/api/$', include(speaker_resource.urls))
)