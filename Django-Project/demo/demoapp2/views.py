from django.shortcuts import render, HttpResponse


def index(request):
    list_of_books = ['Maths', 'Bio', 'OOP', 'Python']
    context = {
        'list_books': list_of_books,
        'list_auths': ['a', 'b', 'c', 'd'],
        'is_login': True
    }
    return render(request, 'index.html', context)
