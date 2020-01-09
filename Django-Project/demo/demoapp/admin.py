from django.contrib import admin

from .models import Student, Department, DepartmentHead, Room,Subject

admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Department)
admin.site.register(DepartmentHead)
admin.site.register(Subject)
