from django.contrib import admin
from django.urls import path
from Events import views as Events_views

urlpatterns = [
    path("EventCreationForm",Events_views.CreatingEvents,name = "EventForm"),
    path("EventUpdationForm/<int:id>/",Events_views.UpdatingEvents,name = "UpdateForm"),
    path("Delete/<int:id>/",Events_views.DeleteEvents,name = "DeleteEvent")
]
