from django.db import models


class Room(models.Model):
    room_no = models.IntegerField()
    floor_no = models.IntegerField()

    def __str__(self):
        return "R " + str(self.room_no) + "F " + str(self.floor_no)


class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    section = models.CharField(max_length=12)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=240)
    code = models.CharField(max_length=4)
    student = models.ManyToManyField(Student,related_name='student')

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
