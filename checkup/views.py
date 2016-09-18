from django.shortcuts import render

# Create your views here.
def index(request):
    patient_list = Patient.objects.filter('doctor')
    template = loader.get_template('template/dashboard_doctor.html')
    context = {
        'patient_list': patient_list,
    }
    return HttpResponse(template.render(context, request))

def patient(request, patient_id):
