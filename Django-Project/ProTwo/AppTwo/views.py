from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse('<em>My Second App</em>')