from django.contrib import admin
from .models import EventCreate

class Events(admin.ModelAdmin):
    list_display=('EventName','EventDescription','EventVenue','EventDate')

admin.site.register(EventCreate,Events)