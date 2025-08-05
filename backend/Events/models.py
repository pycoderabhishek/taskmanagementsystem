from django.db import models

class EventCreate(models.Model):
    EventName = models.CharField(max_length=30)
    EventDescription = models.CharField(max_length=100)
    EventVenue = models.CharField(max_length=30)
    EventDate = models.DateField(default='2025-07-20')
# Create your models here.
