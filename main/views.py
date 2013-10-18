from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from .models import *

def index(request):

    if request.method == 'POST':
        item = request.POST.get('item', None)
        if item is not None:
            Activity.objects.create(person=Person.get_current_person(), item=item)
            return HttpResponseRedirect('/')

    history = Activity.objects.order_by('-timestamp')[:10]
    latest_activity = Activity.get_latest_activity()
    all_people = Person.objects.order_by('pk')
    current_person = Person.get_current_person()

    return render_to_response(
        'main/index.html',
        context_instance = RequestContext(request),
        dictionary = {
            'history': history,
            'today_was_done': Activity.today_was_done(),
            'latest_activity': latest_activity,
            'all_people': all_people,
            'current_person': current_person
        }
    )