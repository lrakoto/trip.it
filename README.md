# trip.it

## User stories
As a user: I want to be able to search for upcoming events at my location or by searching a specific city. I want to be able to add events to my itinerary (TripTree) and get event updates and RSVP if event owner allows. Be able to create/edit personal profile. Stretch goal is to add ability for promotional discounts if booking events through the app.

As an admin: Be able to add, remove and edit events based on location and event dates/times. Be able to create/edit business/personal profile. Booking options and capacity limits. Stretch goal is top lists for accounts with high ratings.

## App Name Ideas
City Trotter
CitiTreat
CitiBeat
CityTrip
CitiLog
CitiBound
CitiVerse
Urban Trotter
Uplanner
EventNow
event.logger
Event.try
Event.ly
eventure
EventVerse
Envent Gator
Vent Finder
url.y
Nexstop
itinera
Hitch Stop
Uvisit
Vizi
Vizi Finder
Vizilog
ViziTrip
Trip.it
TripTree
Trip Journal
Travelocity
travelverse
Travelity
Velity
Travela
Pinstop
Local.xplorer
near.me
near.by
Localify
findry
Urbanaut
Urbanknot
Knotical
xplor
xPlot
xmark
mark.r

## Code Examples
```python
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

```

## Wireframe
![Trip.it Wireframe](public/assets/trip_wire.png)

## ERD
![AutoDex Wireframe](public/assets/trip_it_ERD.png)