from __future__ import unicode_literals
from lumohacks.model import Patient, TimeStampedModel
from django.db import models


class Log(TimeStampedModel):
    patient = models.ForeignKey(Patient)
    name = models.CharField(max_length=128)
    value = models.IntegerField()


class Treatment(TimeStampedModel):
    patient = models.ForeignKey(Patient)
    name = models.CharField(max_length=128)
    value = models.IntegerField()


class Pain(TimeStampedModel):
    patient = models.ForeignKey(Patient)
    location = models.CharField(max_length=128)
    severity = models.IntegerField()

