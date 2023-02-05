from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Student




# Create your views here.







def home(request):
    return render(request, 'home.html')

@login_required
def register(request):
    user= request.user
    if request.method == 'POST':
        name = request.POST['name']
        standard =request.POST['standard']
        school = request.POST['school']
        phone_number= request.POST['phone_number']
        



        if Student.objects.filter(name=name).first() is not None:
            
            Student.user = user
            Student.name = name                                                                                                             
            Student.standard = standard
            Student.school = school
            Student.phone_number=phone_number
            
            Student.save(update_fields=['name','standard','school', 'phone_number'])
        else:    
            student = Student.objects.create( name=name, standard=standard,phone_number=phone_number,school= school)
            student.save()

            student_model=  Student.objects.get(name=name)
            new_profile= Student.objects.create(name=name,standard=standard,phone_number=phone_number,school=school)
            



    else:
            return render(request, 'profile.html')

