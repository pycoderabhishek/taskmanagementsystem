"""
URL configuration for newbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newbackend import views
<<<<<<< HEAD
=======
from Events import views as Events_views
>>>>>>> b205632a24384ff2cf8d7f0b0b139de9e454c5fd
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homepage,name = "homepage"),
<<<<<<< HEAD
    path("Events/", include("Events.urls")),
    
=======
    path("Events/",include("Events.urls"))
>>>>>>> b205632a24384ff2cf8d7f0b0b139de9e454c5fd
]
