from django.shortcuts import render
from django.http import HttpResponse
import json
from codecamp.models import Speaker

def index(request):
    #return render_to_response('codecamp/index.html', {}, context_instance=RequestContext(request))
    return render(request, 'codecamp/index.html')


def speaker_json(request):
    response_data = [str(obj) for obj in Speaker.objects.values()]
    return HttpResponse(json.dumps(response_data), content_type="application/json")
