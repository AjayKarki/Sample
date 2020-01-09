from django.contrib import admin

from demoapp import models

admin.site.register(models.Student)
admin.site.register(models.Room)
admin.site.register(models.Department)
admin.site.register(models.DepartmentHead)
admin.site.register(models.Subject)
