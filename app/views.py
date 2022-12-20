from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, HttpResponse
from trip_it import settings
from .models import Event
import googlemaps
from json import *

events = Event.objects.all()

## EVENTS CRUD ##
class EventCreate(CreateView):
  model = Event
  fields = '__all__'
  success_url = '/events'

class EventUpdate(UpdateView):
  model = Event
  fields = ['name', 'date', 'enddate', 'venueName', 'address', 'description', 'image', 'capacity']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/events/' + str(self.object.pk))

class EventDelete(DeleteView):
  model = Event
  success_url = '/events'



## GOOGLE MAPS API ##

gkey = settings.GMAPS_KEY

# Google maps API Key
gmaps = googlemaps.Client(key=gkey)

# retrieve coordinates for current location
location = gmaps.geolocate()

# Views
def index(request):
    # assign google maps data to variable
    mapdata = {
        'mapdata': location
    }
    # convert data into JSON for use in browser
    mapJSON = dumps(mapdata)
    return render(request, 'index.html', {'location': location, 'googlekey': gkey, 'maps': mapJSON})

def about(request):
    return render(request, 'about.html')

def eventspage(request):
    return render(request, 'events/index.html', {'events': events})

def eventdetails(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/details.html', { 'event': event })