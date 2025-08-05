from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from Events.forms import EventCreateForm
from Events.models import EventCreate

def homepage(request):
    obj= EventCreate.objects.all()
    return render(request,"homepage.html",{"ReadingEvents":obj})

