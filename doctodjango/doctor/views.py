from django.http import HttpResponse
from .models import Doctor, Patient, Rdv


def index(request):
    return HttpResponse("form")


def doctor(request):
    doctors = Doctor.objects.all()
    return HttpResponse(doctors)


def patient(request):
    patients = Patient.objects.all()
    return HttpResponse(patients)


def rdv(request):
    rdvs = Rdv.objects.all()
    return HttpResponse(rdvs)
