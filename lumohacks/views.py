from django.shortcuts import render, redirect
from .model import Doctor,Patient
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        user = User.objects.create_user(request.POST.get('username'), request.POST.get('password'))
        user.save()
        if request.POST.get('type') == 'doctor':
            doctor = Doctor.objects.create(user=user)
            doctor.save()
        else:
            patient = Patient.objects.create(user=user)
            patient.save()
        user = authenticate(username=user.username, password=user.password)
        return redirect('home')
    else:
        return render(request, 'register.html', {})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('home')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html', {'error': 'Authenticate fails'})
    else:
        return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return render(request, 'login.html', {})


@login_required
def home(request):
    if Doctor.objects.filter(user=request.user).exists():
        return render(request, 'dashboard_doctor.html', {})
    else:
        return render(request, 'dashboard_patient.html', {})


def doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'dashboard_doctor.html', {doctor: doctor})


def patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    return render(request, 'dashboard_patient.html', {patient: patient})
