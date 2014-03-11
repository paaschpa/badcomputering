from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import TemplateView
#from codecamp import views
from codecamp.api import SpeakerResource
import dbindexer

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

speaker_resource = SpeakerResource()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', TemplateView.as_view(template_name="home.html")),
    ('^codecamp/$', include('codecamp.urls')),
    #url(r'^codecamp/api/$', views.speaker_json, name='speaker_json'),
    (r'^codecamp/api/', include(speaker_resource.urls)),
    ('^admin/', include(admin.site.urls)),
)
