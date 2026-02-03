from django import forms
from django.contrib.auth import get_user_model
from .models import Appointment, Advisor

User = get_user_model()

class AppointmentForm(forms.ModelForm):
    """Formulaire de prise de rendez-vous"""
    
    class Meta:
        model = Appointment
        fields = ['advisor', 'date', 'time', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['advisor'].queryset = Advisor.objects.all()
        self.fields['advisor'].label = 'Conseiller'
        self.fields['date'].label = 'Date du rendez-vous'
        self.fields['time'].label = 'Heure du rendez-vous'
        self.fields['notes'].label = 'Notes (optionnel)'

class AdvisorFilterForm(forms.Form):
    """Formulaire de filtrage des conseillers"""
    
    speciality = forms.CharField(
        max_length=100,
        required=False,
        label='Spécialité'
    )
    
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date'
    )