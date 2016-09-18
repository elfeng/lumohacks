from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.IntegerField()
    age = models.IntegerField()
    gender = models.IntegerField()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
