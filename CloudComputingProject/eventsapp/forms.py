from django import forms
from .models import Post

class EventsForm(forms.ModelForm):
    event_date = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'],
                               widget=forms.
                               DateTimeInput(attrs={'type': 'datetime-local',
                                                    'class': 'form-control'}))
    class Meta:
        model = Post
        fields = ['event_name', 'event_description', 'location', 'event_date']
        widgets = {'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
                   }


