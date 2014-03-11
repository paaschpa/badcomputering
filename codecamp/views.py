from django.shortcuts import render
from django.template.context import RequestContext


def index(request):
    #return render_to_response('codecamp/index.html', {}, context_instance=RequestContext(request))
    return render(request, 'codecamp/index.html')
