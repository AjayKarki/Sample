from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    room = RoomSerializer()  # one student in one room so many == true not required

    class Meta:
        model = Student
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(
    #     many=True)  # dherai studentxan so many == true i.e one subject is taken by many students
    class Meta:
        model = Subject
        fields = '__all__'
