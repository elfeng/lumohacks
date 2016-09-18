from django.shortcuts import render
from .models import Log, Pain

# Create your views here.
def log (request):
    if request.method == "POST":
        fruit = Log(user=request.COOKIES.get('user_id') ,name="fruit",value=request.POST.get('fruit-option'))
        fruit.save()
        vegetable = Log(user=request.COOKIES.get('user_id') ,name="vegetable",value=request.POST.get('vegetable-option'))
        vegetable.save()
        grain = Log(user=request.COOKIES.get('user_id') ,name="grain",value=request.POST.get('grain-option'))
        grain.save()
        dairy = Log(user=request.COOKIES.get('user_id') ,name="dairy",value=request.POST.get('dairy-option'))
        dairy.save()
        protein = Log(user=request.COOKIES.get('user_id') ,name="protein",value=request.POST.get('protein-option'))
        protein.save()
        fat = Log(user=request.COOKIES.get('user_id') ,name="fat", value=request.POST.get('fat-option'))
        fat.save()
        light = Log(user=request.COOKIES.get('user_id') ,name="light", value=request.POST.get('light'))
        light.save()
        medium = Log(user=request.COOKIES.get('user_id') ,name="medium", value=request.POST.get('medium'))
        medium.save()
        vigorous = Log(user=request.COOKIES.get('user_id') ,name="vigorous", value=request.POST.get('vigorous'))
        vigorous.save()
        pain = Pain(user=request.COOKIES.get('user_id') ,location=request.POST.get('pain'), severity=request.POST.get('severity'))
        pain.save()

    else:
        return render(request, 'dashboard_patient.html', {})

