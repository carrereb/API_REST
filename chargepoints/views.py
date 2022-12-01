from django.shortcuts import render
import json
from django.http import HttpResponse
from chargepoints.models import Chargepoint, Customer
from django.shortcuts import render
from django.http import JsonResponse


def ChargepointToDictionary(chargepoint):
    """
    A utility function to convert object of type Blog to a Python Dictionary
    """
    output = {}
    output["id"] = chargepoint.id
    output["name"] = chargepoint.name
    output["number_of_chargepoint"] = chargepoint.number_of_chargepoint
    output["max_power_w"] = chargepoint.max_power_w

    return output

def chargepoint(request):
    if request.method == 'GET':
        # Multiple Chargepoints
        chargepoints = Chargepoint.objects.all()
        tempChargepoints = []

        for i in range(len(chargepoints)):
            tempChargepoints.append(ChargepointToDictionary(chargepoints[i])) # Converting `QuerySet` to a Python Dictionary

        chargepoints = tempChargepoints

        data = {
            "chargepoints": chargepoints
        }

        return JsonResponse(data)
    else:
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_405_BAD_REQUEST)

def chargepoint_id(request, id):
    # Single Chargepoint
    chargepoint = Chargepoint.objects.get(id = id)

    # Converting `QuerySet` to a Python Dictionary
    chargepoint = ChargepointToDictionary(chargepoint)

    data = {
        "chargepoint": chargepoint
    }

    return JsonResponse(data)



def CustomerToDictionary(chargepoint):
    """
    A utility function to convert object of type Blog to a Python Dictionary
    """
    output = {}
    output["id"] = chargepoint.id
    output["name"] = chargepoint.name
    output["chargepoint"] = chargepoint.chargepoint
    output["total_payed"] = chargepoint.total_payed

    return output

def customers(request):
    # Multiple Customers
    customers = Customer.objects.all()
    tempCustomers = []

    for i in range(len(customers)):
        buffer = CustomerToDictionary(customers[i])
        buffer["chargepoint"] = ChargepointToDictionary(buffer["chargepoint"])
        tempCustomers.append(buffer) # Converting `QuerySet` to a Python Dictionary

    customers = tempCustomers

    data = {
        # "customer": customer,
        "customers": customers
    }

    return JsonResponse(data)

def customers_id(request, id):
    # Single Customer
    customer = Customer.objects.get(id = id)

    # Converting `QuerySet` to a Python Dictionary
    customer = CustomerToDictionary(customer)
    customer["chargepoint"] = ChargepointToDictionary(customer["chargepoint"])

    data = {
        "customer": customer
    }

    return JsonResponse(data)

def chargepoint_post(request):
    chargepoints = json.loads(request.body)
    for chargepoint in chargepoints:
        data = Chargepoint()
        data.name = chargepoint["name"]
        data.number_of_chargepoint = chargepoint["number_of_chargepoint"]
        data.max_power_w = chargepoint["max_power_w"]
        data.save()
