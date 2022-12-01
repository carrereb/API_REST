from django.shortcuts import render
from django.http import HttpResponse

def chargepoint(request):
    return HttpResponse('<h1>Chargepoint</h1>')

def customers(request):
    return HttpResponse('<h1>Customers</h1>')
