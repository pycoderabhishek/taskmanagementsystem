from django.db import models

class EventCreate(models.Model):
    EventName = models.CharField(max_length=30)
    EventDescription = models.CharField(max_length=100)
    EventVenue = models.CharField(max_length=30)
<<<<<<< HEAD
    EventDate = models.DateField(default='01-01-2025')
=======
    EventDate = models.DateField(default='2025-07-20')
>>>>>>> b205632a24384ff2cf8d7f0b0b139de9e454c5fd
# Create your models here.
