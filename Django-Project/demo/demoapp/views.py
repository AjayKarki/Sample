from django.shortcuts import render, HttpResponse, redirect
from .models import Student, Room
from .forms import StudentForm, RoomForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def contact_us(request):
    return render(request, 'contactus.html')


def list_student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        return render(request, 'list_student.html', {'students': students})


def list_room(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        return render(request, 'list_room.html', {'rooms': rooms})


@csrf_exempt
def add_student(request):
    if request.method == 'GET':
        student_form = StudentForm()
        return render(request, 'add_student.html', {'form': student_form})
    elif request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
    return redirect('list_student')


@csrf_exempt
def add_room(request):
    if request.method == 'GET':
        room_form = RoomForm()
        return render(request, 'add_room.html', {'form': room_form})
    elif request.method == 'POST':
        room_form = RoomForm(request.POST)
        if room_form.is_valid():
            room_form.save()
    return redirect('list_room')


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('list_student')