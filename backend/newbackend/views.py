from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from Events.forms import EventCreateForm
from Events.models import EventCreate

def homepage(request):
<<<<<<< HEAD
    events= EventCreate.objects.all()
    
<<<<<<< HEAD
    return render(request,"homepage.html",{"events":events})

def CreatingEvents(request):
    form = EventCreateForm(request.POST)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect("homepage")
        else :
            HttpResponse("unsuccess")
    else:
        form = EventCreateForm
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
=======
    obj= EventCreate.objects.all()
    return render(request,"homepage.html",{"events":obj})
>>>>>>> 307a02069acff0383bd3afd66cf0e6a1ca0821f4
=======
    return render(request,"homepage.html",{"events":obj})

    
>>>>>>> b205632a24384ff2cf8d7f0b0b139de9e454c5fd

