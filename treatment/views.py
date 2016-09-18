from django.shortcuts import render
from .models import Log, Pain

# Create your views here.
def log (request):
    if request.method == "POST":
        fruit = Log(name="fruit",value=request.POST.get('fruit-option'))
        fruit.save()
        vegetable = Log(name="vegetable",value=request.POST.get('vegetable-option'))
        vegetable.save()
        grain = Log(name="grain",value=request.POST.get('grain-option'))
        grain.save()
        dairy = Log(name="dairy",value=request.POST.get('dairy-option'))
        dairy.save()
        protein = Log(name="protein",value=request.POST.get('protein-option'))
        protein.save()
        fat = Log(name="fat", value=request.POST.get('fat-option'))
        fat.save()
        light = Log(name="light", value=request.POST.get('light'))
        light.save()
        medium = Log(name="medium", value=request.POST.get('medium'))
        medium.save()
        vigorous = Log(name="vigorous", value=request.POST.get('vigorous'))
        vigorous.save()
        pain = Pain(location=request.POST.get('pain'), severity=request.POST.get('severity'))
        pain.save()

    else:
        return render(request, 'dashboard_patient.html', {})

