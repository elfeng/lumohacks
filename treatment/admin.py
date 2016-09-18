from django.contrib import admin
from .models import Log, Treatment, Pain


class LogAdmin(admin.ModelAdmin):
    list_display = ('patient', 'name', 'value')


class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'name', 'value')


class PainAdmin(admin.ModelAdmin):
    list_display = ('patient', 'location', 'severity')


admin.site.register(Log, LogAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Pain, PainAdmin)
