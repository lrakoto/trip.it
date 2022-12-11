from django.shortcuts import render

class Event:
    def __init__(self, userId, name, date, location, description, image, capacity):
        self.name = name
        self.userId = userId
        self.date = date
        self.location = location
        self.description = description
        self.image = image
        self.capacity = capacity

events = [
    Event(
        1, 
        'Event 1', 
        'January', 
        'Los Angeles', 
        'this is a cool event', 
        'https://unsplash.com/photos/QQMnCX3B07c',
        200,
    ),
    Event(
        1, 
        'Event 2', 
        'February', 
        'Los Angeles', 
        'this is a cool event #2', 
        'https://unsplash.com/photos/QQMnCX3B07c',
        200,
    ),
    
]

# Views
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def eventspage(request):
  return render(request, 'events/index.html', { 'events': events })