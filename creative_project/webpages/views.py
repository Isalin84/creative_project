# webpages/views.py

from django.shortcuts import render

def data_view(request):
    return render(request, 'data.html')

def test_view(request):
    return render(request, 'test.html')

def home_view(request):
    return render(request, 'home.html')
