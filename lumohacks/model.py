from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
