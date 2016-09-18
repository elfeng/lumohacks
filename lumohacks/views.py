from django.shortcuts import render, redirect
from .model import Doctor,Patient
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
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


def logout_view(request):
    logout(request)
    return render(request, 'registration/login.html', {})

@login_required
def home(request):
    if Doctor.objects.filter(user=request.user).exists():
        patient_list = Patient.objects.all()
        response = render(request, 'dashboard_doctor.html', {'patient_list': patient_list})
        response.set_cookie('user_id', request.user)
        return response
    else:
        if not Patient.objects.get(user=request.user).weight is None:
            response = render(request, 'dashboard_patient.html', {})
            response.set_cookie('user_id', request.user)
            return response
        else:
            response = render(request, 'setting.html', {})
            response.set_cookie('user_id', request.user)
            return response

def setting(request):
    if request.method == "POST":
        patient = Patient.objects.get(user= request.user)
        patient.name = request.POST.get('name')
        patient.weight = int(request.POST.get('weight'))
        patient.age = int(request.POST.get('age'))
        patient.gender = int(request.POST.get('gender'))
        patient.blood_pressure = int(request.POST.get('blood-pressure'))
        patient.smoke = int(request.POST.get('smoke'))
        patient.constipation = int(request.POST.get('constipation'))
        patient.diabetes = int(request.POST.get('diabetes'))
        patient.save()
        return render(request, 'dashboard_patient.html', {})
    else:
        return render(request, 'setting.html', {})