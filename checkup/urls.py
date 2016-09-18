from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<patient_id>[0-9]+)/$', views.patient, name='patient')
]