from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import TemplateView
from codecamp import views
import dbindexer

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', TemplateView.as_view(template_name="home.html")),
    ('^codecamp/$', include('codecamp.urls')),
    url(r'^codecamp/api/$', views.speaker_json, name='speaker_json'),
    ('^admin/', include(admin.site.urls)),
)
