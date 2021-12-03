from django.contrib.auth import login
from django.http import HttpResponse
from .models import Doctor, Patient, Rdv
from .forms import DoctorForm, NewUserForm
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rdv')
    else:
        form = DoctorForm()

    return render(request, 'index.html', {'form': form})


def doctor(request):
    doctors = Doctor.objects.all()
    return HttpResponse(doctors)


def patient(request):
    patients = Patient.objects.all()
    return HttpResponse(patients)


def rdv(request):
    rdvs = Rdv.objects.all()
    return HttpResponse(rdvs)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})
