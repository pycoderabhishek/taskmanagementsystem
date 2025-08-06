<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import EventCreateForm
from .models import EventCreate
def CreatingEvents(request):
    if(request.method == 'POST'):
        form = EventCreateForm(request.POST)
        if(form.is_valid()):
            print("success")
=======
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from .forms import EventCreateForm
from .models import EventCreate

def CreatingEvents(request):
    form = EventCreateForm(request.POST)
    if(request.method == 'POST'):
        if(form.is_valid()):
>>>>>>> b205632a24384ff2cf8d7f0b0b139de9e454c5fd
            form.save()
            return redirect("homepage")
        else :
            HttpResponse("unsuccess")
    else:
<<<<<<< HEAD
        form = EventCreateForm()
=======
        form = EventCreateForm
>>>>>>> b205632a24384ff2cf8d7f0b0b139de9e454c5fd
    return render(request,"eventcreateform.html",{'form':form})

def UpdatingEvents(request,id):
    event = get_object_or_404(EventCreate,id=id)
    if(request.method == 'POST'):
        form = EventCreateForm(request.POST, instance=event)
        if(form.is_valid()):
            form.save()
            return redirect("homepage")
        else :
            HttpResponse("unsuccess")
    else:
        form = EventCreateForm(instance=event)
    return render(request,"eventupdateform.html",{'form':form,'event':event})

def DeleteEvents(request,id):
    event = get_object_or_404(EventCreate,id=id)
    event.delete()
<<<<<<< HEAD
    return redirect("homepage")    

=======
    return redirect("homepage")
>>>>>>> b205632a24384ff2cf8d7f0b0b139de9e454c5fd
