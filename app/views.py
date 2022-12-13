from django.shortcuts import render
from .models import Event

events = Event.objects.all()

# Views
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def eventspage(request):
  return render(request, 'events/index.html', { 'events': events })