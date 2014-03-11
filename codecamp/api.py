from tastypie.resources import ModelResource
from codecamp.models import Speaker


class SpeakerResource(ModelResource):
    class Meta:
        queryset = Speaker.objects.all()
        resource_name = 'speaker'