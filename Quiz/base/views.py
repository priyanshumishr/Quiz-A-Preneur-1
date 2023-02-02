

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


# Create your views here.

from django.http import HttpResponse





def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST["name"]
        standard = request.POST["standard"]
        school = request.POST["school"]
        
        if register.objects.filter(name=name).first() is not None:
            register.objects.filter(name=name).first().delete()
        student = register.objects.create(name=name,standard=standard,school=school)
        student.save()
        return redirect('index')

    else:
        return render(request, 'profile.html')

