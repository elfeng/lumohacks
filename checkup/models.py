from __future__ import unicode_literals

from django.db import models
from lumohacks.model import Patient, Doctor, TimeStampedModel


TREATMENT_CHOICES = (
    (0, 'Surgery'),
    (1, 'Chemotherapy'),
    (2, 'Radiation Therapy'),
)


class Diagnose(TimeStampedModel):
    patient = models.ForeignKey(Patient)
    note = models.TextField()
    treatment = models.IntegerField(choices=TREATMENT_CHOICES)
    duration = models.IntegerField()


class Matrix(models.Model):
    name = models.CharField(max_length=128)
    matrix = models.TextField()
