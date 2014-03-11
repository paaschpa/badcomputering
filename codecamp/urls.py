from django.conf.urls import *
from codecamp import views


urlpatterns = patterns('codecamp.views',
    url(r'^$', views.index, name='index'),
)