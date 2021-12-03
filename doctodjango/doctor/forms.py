from django import forms
from .models import Doctor, Rdv
from django.forms import ModelForm, fields


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Rdv
        fields = '__all__'
        #doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), initial=0)
        #Rdv = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
