from django.shortcuts import render
from my_app.models import Student
from django.http import HttpResponse

# Create your views here.

def index(request):
    user_list = Student.objects.all()
    user_dict = {"students":user_list}
    return render(request, 'my_app/index.html', context=user_dict)

def math(request):
    math_students = Student.objects.filter(subject='Mathematics')
    math_dict = {"students":math_students}
    return render(request, 'my_app/math.html', context=math_dict) 

def biology(request):
    bio_students = Student.objects.filter(subject='Biology')
    bio_dict = {"students":bio_students}
    return render(request, 'my_app/biology.html', context=bio_dict) 


def geometry(request):
    geometry_students = Student.objects.filter(subject='Geometry')
    geometry_dict = {"students":geometry_students}
    return render(request, 'my_app/geometry.html', context=geometry_dict) 


def martial_arts(request):
    martial_students = Student.objects.filter(subject='Martial Arts')
    martial_dict = {"students":martial_students}
    return render(request, 'my_app/martial_arts.html', context=martial_dict) 


def physics(request):
    physics_students = Student.objects.filter(subject='Physics')
    physics_dict = {"students":physics_students}
    return render(request, 'my_app/physics.html', context=physics_dict) 
    



