
from django.contrib import admin
from django.urls import path
from .views import contact_us,list_student

urlpatterns = [
    path('contact-us/', contact_us, name='contact-us'),
    path('list-students/',list_student,name='list_student')
]
