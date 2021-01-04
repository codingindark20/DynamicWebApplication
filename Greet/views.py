from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'User'})

def vat(request):
    value = int(request.GET['amount'])
    result = value * 0.13
    return render(request, 'result.html', {'Result': result})