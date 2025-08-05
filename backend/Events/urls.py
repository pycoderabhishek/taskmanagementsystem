from django.contrib import admin
from django.urls import path
from Events import views
path("EventCreationForm",views.CreatingEvents,name = "EventForm"),
path("EventUpdationForm/<int:id>/",views.UpdatingEvents,name = "UpdateForm"),
path("Delete/<int:id>/",views.DeleteEvents,name = "DeleteEvent")