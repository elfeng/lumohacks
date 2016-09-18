from django.contrib import admin

# Register your models here.
from .models import Patient, Doctor, Diagnose


class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'age', 'gender')


class DoctorAdmin(admin.ModelAdmin):
    pass


class DoctorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)