from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import EventCreateForm
from .models import EventCreate
def CreatingEvents(request):
    form = EventCreateForm(request.POST)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect("homepage")
        else :
            HttpResponse("unsuccess")
    else:
        form = EventCreateForm()
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
    return redirect("homepage")    

