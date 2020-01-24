from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete


class Room(models.Model):
    room_no = models.IntegerField()
    floor_no = models.IntegerField()
    numbers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "R-" + str(self.room_no) + " F-" + str(self.floor_no)


class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    section = models.CharField(max_length=12)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to='student_pics', default='test.png')

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=240)
    code = models.CharField(max_length=4)
    student = models.ManyToManyField(Student, related_name='student')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=20, null=False)
    code = models.IntegerField()

    def __str__(self):
        return self.name


class DepartmentHead(models.Model):
    name = models.CharField(max_length=255)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# @receiver(post_save, sender=Student )
# def increment_room(instance):
#     room = instance.room
#     room.numbers +=1
#     room.save()