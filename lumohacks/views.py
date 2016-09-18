from django.shortcuts import render
from .model import Doctor,Patient

def home(request):
    return render(request, 'home.html', {})

def doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'doctor.html', {doctor: doctor})

def patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    return render(request, 'patient.html', {patient: patient})