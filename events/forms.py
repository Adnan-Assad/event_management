from django import forms
from events.models import Category, Event, Participant

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets ={
            'name': forms.TextInput(attrs={"placeholder":"Event Name"}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'date': forms.DateInput(attrs={'type':'date'}),
            'time':forms.TimeInput(attrs={'type':'time'}),
            'location':forms.TextInput(attrs={'placeholder':'Event Location'})
        }

class ParticipantModelForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']

        widgets = {
            'events': forms.CheckboxSelectMultiple()
        }