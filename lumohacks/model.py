from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return unicode(self.user.username)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    doctor = models.ForeignKey(Doctor, null=True)
    weight = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    gender = models.IntegerField(null=True)
    blood_pressure = models.IntegerField(null=True)
    smoking = models.IntegerField(null=True)
    constipation = models.IntegerField(null=True)
    diabetes = models.IntegerField(null=True)

    def __unicode__(self):
        return unicode(self.user.username)