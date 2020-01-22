from django.urls import path
from demoapp import views

urlpatterns = [
    path('contact-us/', views.contact_us, name='contact-us'),
    path('list-students/', views.list_student, name='list_student'),
    path('add_student/', views.add_student, name='add_student'),
    path('list-room/', views.ListRooms.as_view(), name='list_room'),
    path('add_room/', views.add_room, name='add_room'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('edit_student/<int:id>/', views.EditStudent.as_view(), name='edit_student'),
    path('detail_student/<int:id>/',views.RoomDetail.as_view(),name='detail_room'),

]
