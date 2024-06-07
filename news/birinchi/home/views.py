from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    
    name = "Husniddin"
    
    return render(request, 'index.html', {'name':name})