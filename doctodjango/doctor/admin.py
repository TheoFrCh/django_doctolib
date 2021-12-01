from django.contrib import admin
from .models import Doctor, Patient, Rdv

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Rdv)