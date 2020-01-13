from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
    path('contact-us/', views.contact_us, name='contact-us'),
    path('list-students/', views.list_student, name='list_student'),
    path('add_student/', views.add_student, name='add_student'),
    path('list-room/', views.list_room, name='list_room'),
    path('add_room/', views.add_room, name='add_room'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
]
