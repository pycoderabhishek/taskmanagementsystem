from django import forms
from .models import EventCreate

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = EventCreate
        fields = "__all__"

class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = EventCreate
        fields = "__all__"