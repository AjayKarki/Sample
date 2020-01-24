from django.forms import ModelForm
from .models import Student, Room
from django import forms
from django.contrib.auth.models import User


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_roll(self):
        roll =  self.cleaned_data.get('roll')
        if roll <= 0:
            raise forms.ValidationError("Roll cant be less than 0 or 0")
        return roll


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    conform_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        conform_password = cleaned_data.get('conform_password')
        email = cleaned_data.get('email')
        if password != conform_password:
            raise forms.ValidationError('Password must match')

        if not email.endswith('.edu'):
            raise forms.ValidationError('Email must be .edu')
