from django import forms
from .models import Doctor


class DoctorForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), initial=0)
