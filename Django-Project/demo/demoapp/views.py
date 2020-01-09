from django.shortcuts import render, HttpResponse
from .models import Student
from .forms import StudentForm


def contact_us(request):
    return render(request, 'contactus.html')


def list_student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        return render(request, 'list_student.html', {'students': students})


def add_student(request):
    form = StudentForm
