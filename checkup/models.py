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
    doctor = models.ForeignKey(Doctor)
    note = models.TextField()
    treatment = models.IntegerField(choices=TREATMENT_CHOICES)
    duration = models.IntegerField()
    blood_pressure = models.IntegerField(null=True)
    smoking = models.IntegerField(null=True)
    constipation = models.IntegerField(null=True)
    diabetes = models.IntegerField(null=True)