from django.shortcuts import render, HttpResponse
from trip_it import settings
from .models import Event

events = Event.objects.all()
gkey = settings.GMAPS_KEY

# Views

def index(request):
    return render(request, 'index.html', {'googlekey': gkey})

def test(request):
    return HttpResponse(f'HEY:{gkey}')

def about(request):
    return render(request, 'about.html')


def eventspage(request):
    return render(request, 'events/index.html', {'events': events})


def eventdetails(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/details.html', { 'event': event })