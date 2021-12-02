from django.http import HttpResponse
from .models import Doctor, Patient, Rdv
from .forms import DoctorForm
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
        return render('/')
    else:
        form = DoctorForm()

    return render(request, 'index.html', {'form': form})

    #context = {}
    #context['form'] = DoctorForm()
    #return render(request, "index.html", context)


def doctor(request):
    doctors = Doctor.objects.all()
    return HttpResponse(doctors)


def patient(request):
    patients = Patient.objects.all()
    return HttpResponse(patients)


def rdv(request):
    rdvs = Rdv.objects.all()
    return HttpResponse(rdvs)
