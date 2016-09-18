from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor)
    weight = models.IntegerField()
    age = models.IntegerField()
    gender = models.IntegerField()
    blood_pressure = models.IntegerField(null=True)
    smoking = models.IntegerField(null=True)
    constipation = models.IntegerField(null=True)
    diabetes = models.IntegerField(null=True)
