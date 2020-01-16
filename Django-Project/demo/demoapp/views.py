from django.shortcuts import render, HttpResponse, redirect
from .models import Student, Room
from .forms import StudentForm, RoomForm
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


def add_student(request):
    if request.method == 'GET':
        student_form = StudentForm()
        print(student_form)
        return render(request, 'add_student.html', {'form': student_form})
    elif request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            student_form.save()
            messages.info(request, "Addition Successful")
    return redirect('list_student')


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
    try:
        student = Student.objects.get(id=id)
        student.delete()
        messages.success(request, "Deleted successfully")
        return redirect('list_student')
    except:
        messages.error(request, 'Student with id' + str(id) + 'not found')
        return redirect('list_student')


def edit_student(request, id):
    if request.method == 'GET':
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
        return render(request, 'edit_student.html', {'form': form, "student_id": id})
    elif request.method == 'POST':
        student = Student.objects.get(id=id)
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'edit_student.html', {'form': form, "student_id": id})
    return redirect('list_student')
