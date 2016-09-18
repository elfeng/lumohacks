from __future__ import unicode_literals

from django.db import models
from lumohacks.model import Patient, Doctor, TimeStampedModel


class Diagnose(TimeStampedModel):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    note = models.TextField()
    treatment = models.CharField(max_length=128)
    duration = models.DecimalField(decimal_places=1, max_digits=5)
