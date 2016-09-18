from django.shortcuts import render
from .model import Doctor,Patient
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def register(request):
    if request.method == "POST":
        user = User.objects.create_user(request.POST.get('username'), request.POST.get('password'))
        user.save()
        user = authenticate(username=user.username, password=user.password)
        if request.POST.get('type') == 'doctor':
            doctor = Doctor.objects.create(user=user)
            doctor.save()
            return render(request, 'dashboard_doctor.html', {})
        else:
            patient = Patient.objects.create(user=user)
            patient.save()
            return render(request, 'dashboard_patient.html', {})
    else:
        return render(request, 'register.html', {})


def login(request):
    if request.method == "POST":
        user = authenticate(request.POST.get('username'), request.POST.get('password'))
        if user is not None:
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
    else:
        return render(request, 'login.html', {})


def home(request):
    return render(request, 'home.html', {})

def doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'doctor.html', {doctor: doctor})

def patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    return render(request, 'patient.html', {patient: patient})
