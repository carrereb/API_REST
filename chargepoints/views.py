from django.shortcuts import render
from django.http import HttpResponse
from chargepoints.models import Chargepoint, Customer
from django.shortcuts import render

def chargepoint(request):
    chargepoints = Chargepoint.ojects.all()
    return render(request, 'chargepoints/chargepoints.json')

def customers(request):
    customers = Customer.ojects.all()
    return HttpResponse('<h1>Customers</h1>')
