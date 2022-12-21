from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import transaction
from trip_it import settings
from .models import Event
from .forms import RegisterForm
import re
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


# Views
def index(request):
    # retrieve coordinates for current location
    location = gmaps.geolocate()
    eventAddressList = []
    for event in events:
        aMarker = gmaps.geocode(event.address)
        eventAddressList.append({
            'id': event.pk,
            'gmapdata': aMarker,
            'name': event.name,
            'image': event.image,
            'description': event.description
        })

    # assign google maps data to variable
    mapdata = {
        'mapdata': location
    }
    eventAddressListData = {
        'addressList': eventAddressList
    }
    # convert data into JSON for use in browser
    mapJSON = dumps(mapdata)
    eventsAddressListJSON = dumps(eventAddressListData)
    currentUser = request.user
    return render(request, 'index.html', {'location': location, 'googlekey': gkey, 'maps': mapJSON, 'addresses': eventsAddressListJSON, 'c_user': currentUser })

@login_required(login_url='/login')
def profile(request, user_id):
    user = User.objects.get(id=user_id)
    events = Event.objects.filter(userId=user)
    return render(request, 'profile.html', {'user_id': user_id, 'user': user, 'events': events})

@login_required(login_url='/login')
def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', { 'form': form })

def eventspage(request):
    return render(request, 'events/index.html', {'events': events})

def eventdetails(request, event_id):
    event = Event.objects.get(id=event_id)
    urlString = event.address
    reps = {' ': '+', ',': '%2C'}

    ## String replacer from https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729 ##
    def multireplace(string, replacements, ignore_case=False):
        if not replacements:
            # Edge case that'd produce a funny regex and cause a KeyError
            return string
        
        # If case insensitive, we need to normalize the old string so that later a replacement
        # can be found. For instance with {"HEY": "lol"} we should match and find a replacement for "hey",
        # "HEY", "hEy", etc.
        if ignore_case:
            def normalize_old(s):
                return s.lower()

            re_mode = re.IGNORECASE

        else:
            def normalize_old(s):
                return s

            re_mode = 0

        replacements = {normalize_old(key): val for key, val in replacements.items()}
        
        # Place longer ones first to keep shorter substrings from matching where the longer ones should take place
        # For instance given the replacements {'ab': 'AB', 'abc': 'ABC'} against the string 'hey abc', it should produce
        # 'hey ABC' and not 'hey ABc'
        rep_sorted = sorted(replacements, key=len, reverse=True)
        rep_escaped = map(re.escape, rep_sorted)
        
        # Create a big OR regex that matches any of the substrings to replace
        pattern = re.compile("|".join(rep_escaped), re_mode)
        
        # For each match, look up the new string in the replacements, being the key the normalized old string
        return pattern.sub(lambda match: replacements[normalize_old(match.group(0))], string)

    formattedString = multireplace(urlString, reps)

    addressCoords = gmaps.geocode(event.address)
    mapdata = {
        'mapdata': addressCoords
    }
    mapJSON = dumps(mapdata)
    return render(request, 'events/details.html', { 'event': event, 'gmapdata': mapJSON, 'googlekey': gkey, 'url': formattedString })

def flush_transaction():
    transaction.commit()