from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import Student, Room, Subject
from .forms import StudentForm, RoomForm, LoginForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

@login_required(login_url='login/')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login/')
def contact_us(request):
    return render(request, 'contactus.html')


@login_required(login_url='login/')
def list_student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        return render(request, 'list_student.html', {'students': students})


@login_required(login_url='login/')
def list_room(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        return render(request, 'room_list.html', {'rooms': rooms})


@login_required(login_url='login/')
def add_student(request):
    if request.method == 'GET':
        student_form = StudentForm()
        return render(request, 'add_student.html', {'form': student_form})
    elif request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            student_form.save()
            messages.info(request, "Addition Successful")
        else:
            messages.error(request, student_form.errors)
            student_form = StudentForm(request.POST)
            return render(request, "add_student.html", {'form': student_form})
    return redirect('list_student')


@login_required(login_url='login/')
def add_room(request):
    if request.method == 'GET':
        room_form = RoomForm()
        return render(request, 'add_room.html', {'form': room_form})
    elif request.method == 'POST':
        room_form = RoomForm(request.POST)
        if room_form.is_valid():
            room_form.save()
    return redirect('list_room')


@login_required(login_url='login/')
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        messages.success(request, "Deleted successfully")
        return redirect('list_student')
    except:
        messages.error(request, 'Student with id' + str(id) + 'not found')
        return redirect('list_student')


# @login_required(login_url='login/')
# def edit_student(request, id):
class EditStudent(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):
        # if request.method == 'GET':
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
        return render(request, 'edit_student.html', {'form': form, "student_id": id})

    def post(self, request, id):
        # elif request.method == 'POST':
        student = Student.objects.get(id=id)
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_student')
        else:
            return render(request, 'edit_student.html', {'form': form, "student_id": id})


def user_login(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')  # duitai same ho
        user = authenticate(username=username, password=password)
        if user:
            login(request, user=user)
            return redirect('list_student')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('user_login')


def user_logout(request):
    logout(request)
    return redirect('user_login')


def user_register(request):
    if request.method == 'GET':
        register_form = RegistrationForm()
        return render(request, 'register.html', {'register_form': register_form})
    elif request.method == 'POST':
        user = RegistrationForm(request.POST)
        if user.is_valid():
            user = user.save()
            user.set_password(user.password)
            user.save()
            return redirect('user_login')
        else:
            user_register = RegistrationForm(request.POST)
            return render(request, 'register.html', {'register_form': user_register})


class ListRooms(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    queryset = Room.objects.all()
    template_name = 'room_list.html'


class ListSubjects(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    queryset = Student.objects.all()
    template_name = 'subject_list.html'


class RoomDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    template_name = 'detail_room.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Room, id=self.kwargs['id'])


class RoomCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    template_name = 'room_create.html'
    form_class = RoomForm
    success_url = reverse_lazy('list_room')


class RoomUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'room_update.html'
    form_class = RoomForm
    login_url = '/login/'

    def get_object(self, queryset=None):
        return get_object_or_404(Room, id=self.kwargs['id'])

    def get_success_url(self):
        return reverse('list_room')


class RoomDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'delete.html'
    login_url = '/login/'

    def post(self, request, *args, **kwargs):
        try:
            room = Room.objects.get(id=self.kwargs['id'])
            room.delete()
            return redirect('list_room')
        except:
            messages.error(request, "Cant delete")
            return redirect('list_room')

    def get_object(self, queryset=None):
        return get_object_or_404(Room, id=self.kwargs['id'])

    def get_success_url(self):
        return reverse('list_room')


@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_serializer = StudentSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=200)
        else:
            return HttpResponse(status=400)


@csrf_exempt
def student_api_detail(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)


