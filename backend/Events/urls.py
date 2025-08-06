from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from Events import views
urlpatterns = [
path("EventCreationForm",views.CreatingEvents,name = "EventForm"),
path("EventUpdationForm/<int:id>/",views.UpdatingEvents,name = "UpdateForm"),
path("Delete/<int:id>/",views.DeleteEvents,name = "DeleteEvent")
]
=======
from Events import views as Events_views

urlpatterns = [
    path("EventCreationForm",Events_views.CreatingEvents,name = "EventForm"),
    path("EventUpdationForm/<int:id>/",Events_views.UpdatingEvents,name = "UpdateForm"),
    path("Delete/<int:id>/",Events_views.DeleteEvents,name = "DeleteEvent")
]
>>>>>>> b205632a24384ff2cf8d7f0b0b139de9e454c5fd
