# school_roster_app/views.py

from django.shortcuts import render
from .models import School # import our School class

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    pass # implement


def staff_detail(request, employee_id):
    pass # implement


def list_students(request):
    pass # implement


def student_detail(request, student_id):
    pass # implement