import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=100)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    capacity = models.IntegerField()
    created = models.DateTimeField('date published')

    def __str__(self):
            return self.name, self.date, self.location, self.description, self.image

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)