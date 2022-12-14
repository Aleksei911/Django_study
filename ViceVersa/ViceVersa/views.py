from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html', {'greeting': 'Hello'})


def reverse(request):
    user_text = request.GET['usertext']
    return render(request, 'reverse.html', {'usertext': user_text})