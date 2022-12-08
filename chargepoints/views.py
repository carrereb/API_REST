from chargepoints.models import Chargepoint, Customer
from django.http import HttpResponse, JsonResponse
from chargepoints.serializers import ChargepointSerializer, CustomerSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def chargepoint_get_list(request):
    if request.method != 'GET':
        return HttpResponse("Error, wrong method", status=405)
    data = Chargepoint.objects.all()
    serializer = ChargepointSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def chargepoint_get_single(request, pk):
    if request.method != 'GET':
        return HttpResponse("Error, wrong method", status=405)
    try:
        data = Chargepoint.objects.get(pk=pk)  # Returns a single object that respect the condition. 
        # If there are 0 ore more than 1, raise exceptions
    except Chargepoint.DoesNotExist:  # Raised when there's no object
        return HttpResponse("Object not found", status=404)  # 404 is Not Found
    serializer = ChargepointSerializer(data)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def chargepoint_post_single(request):
    if request.method != 'POST':
        return HttpResponse("Error, wrong method", status=405)
    serializer = ChargepointSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    else:
        dico = {}
        dico["Erreur"]= True
        return JsonResponse(serializer.data)
    return HttpResponse(f"Error, not acceptable", status=406)

@api_view(['DELETE'])
def chargepoint_delete_single(request, pk):
    if request.method != 'DELETE':
        return HttpResponse("Error, wrong method", status=405)
    try:
        data = Chargepoint.objects.get(pk=pk)  # Returns a single object that respect the condition. 
        # If there are 0 ore more than 1, raise exceptions
    except Chargepoint.DoesNotExist:  # Raised when there's no object
        return HttpResponse("Object not found", status=404)  # 404 is Not Found
    data.delete()
    return HttpResponse("Delete", status=200)


@api_view(['GET'])
def customers_get_list(request):
    if request.method != 'GET':
        return HttpResponse("Error, wrong method", status=405)
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def customers_get_single(request, pk):
    if request.method != 'GET':
        return HttpResponse("Error, wrong method", status=405)
    try:
        data = Customer.objects.get(pk=pk)  # Returns a single object that respect the condition. 
        # If there are 0 ore more than 1, raise exceptions
    except Customer.DoesNotExist:  # Raised when there's no object
        return HttpResponse("Object not found", status=404)  # 404 is Not Found
    serializer = CustomerSerializer(data)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def customers_post_single(request, pk):
    if request.method != 'POST':
        return HttpResponse("Error, wrong method", status=405)
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        customer = serializer.save()
        try:
            customer.chargepoint = Chargepoint.objects.get(id=pk)  # Returns a single object that respect the condition. 
            # If there are 0 ore more than 1, raise exceptions
        except Customer.DoesNotExist:  # Raised when there's no object
            return HttpResponse("Object not found", status=404)  # 404 is Not Found
        customer.save()
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse("Error, not acceptable", status=406)

@api_view(['DELETE'])
def customers_delete_single(request, pk):
    if request.method != 'DELETE':
        return HttpResponse("Error, wrong method", status=405)
    try:
        data = Customer.objects.get(pk=pk)  # Returns a single object that respect the condition. 
        # If there are 0 ore more than 1, raise exceptions
    except Customer.DoesNotExist:  # Raised when there's no object
        return HttpResponse("Object not found", status=404)  # 404 is Not Found
    data.delete()
    return HttpResponse("No content", status=204)
