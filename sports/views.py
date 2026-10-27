
from django.shortcuts import render


def home(request):
    return render(request, 'sports/home.html')


def football(request):
    return render(request, 'sports/football.html')


def hockey(request):
    return render(request, 'sports/hockey.html')


def basketball(request):
    return render(request, 'sports/basketball.html')
