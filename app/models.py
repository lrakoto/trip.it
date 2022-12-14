import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=100)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    enddate = models.DateTimeField(default=datetime.datetime.now, blank=True)
    venueName = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=300)
    capacity = models.IntegerField()
    attendees = models.IntegerField(default=0)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.venueName} {self.address} {self.description} {self.image}'