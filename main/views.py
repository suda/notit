from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from .models import *

def index(request):
    history = Activity.objects.order_by('-timestamp')[:10]

    return render_to_response(
        'main/index.html',
        context_instance = RequestContext(request),
        dictionary = {
            'history': history,
            'today_was_done': Activity.today_was_done(),
            'latest_activity': Activity.get_latest_activity()
        }
    )