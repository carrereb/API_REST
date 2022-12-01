from chargepoints.models import Chargepoint, Customer
# from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
# from rest_framework.parsers import JSONParser 
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from chargepoints.serializers import ChargepointSerializer, CustomerSerializer


class ChargepointAPIView(APIView):
 
    def get(self, *args, **kwargs):
        chargepoints = Chargepoint.objects.all()
        serializer = ChargepointSerializer(chargepoints, many=True)
        return Response(serializer.data)

class ChargepointViewsetGet(ReadOnlyModelViewSet):

    serializer_class = ChargepointSerializer

    def get_queryset(self):
        queryset = Chargepoint.objects.all()

        chargepoint_id = self.request.GET.get('chargepoint_id')
        if chargepoint_id is not None:
            queryset = queryset.filter(chargepoint_id=chargepoint_id)
        return queryset

class ChargepointViewsetPost(ModelViewSet):

    serializer_class = ChargepointSerializer
    queryset = Chargepoint.objects.all()

    # def get_queryset(self):
    #     return HttpResponseBadRequest("Erreur 405")
        # queryset = Chargepoint.objects.all()

        # chargepoint_id = self.request.GET.get('chargepoint_id')
        # if chargepoint_id is not None:
        #     queryset = queryset.filter(chargepoint_id=chargepoint_id)
    #     # return queryset

    # def post(self, request, *args, **kwargs):
    #     self.queryset = Chargepoint.objects.all()
    #     if request.method == 'POST':
    #         data = {
    #             'name': request.data['name'],
    #             'number_of_chargepoint': request.data['number_of_chargepoint'],
    #             'max_power_w': request.data['max_power_w'],
    #         }
    #     serializer = ChargepointSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomerAPIView(APIView):
 
    def get(self, *args, **kwargs):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class CustomerViewsetPost(ModelViewSet):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    # def get_queryset(self):
    #     return HttpResponseBadRequest("Erreur 405")

class CustomerViewsetGet(ReadOnlyModelViewSet):

    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()

        customer_id = self.request.GET.get('customer_id')
        if customer_id is not None:
            queryset = queryset.filter(customer_id=customer_id)
        return queryset


# def ChargepointToDictionary(chargepoint):
#     """
#     A utility function to convert object of type Blog to a Python Dictionary
#     """
#     output = {}
#     output["id"] = chargepoint.id
#     output["name"] = chargepoint.name
#     output["number_of_chargepoint"] = chargepoint.number_of_chargepoint
#     output["max_power_w"] = chargepoint.max_power_w

#     return output

# def chargepoint(request):
#     if request.method == 'GET':
#         # Multiple Chargepoints
#         chargepoints = Chargepoint.objects.all()
#         tempChargepoints = []

#         for i in range(len(chargepoints)):
#             tempChargepoints.append(ChargepointToDictionary(chargepoints[i])) # Converting `QuerySet` to a Python Dictionary

#         chargepoints = tempChargepoints

#         data = {
#             "chargepoints": chargepoints
#         }

#         return JsonResponse(data)
#     # else:
#     #     return JsonResponse(tutorial_serializer.errors, status=status.HTTP_405_BAD_REQUEST)

# def chargepoint_id(request, id):
#     # Single Chargepoint
#     chargepoint = Chargepoint.objects.get(id = id)

#     # Converting `QuerySet` to a Python Dictionary
#     chargepoint = ChargepointToDictionary(chargepoint)

#     data = {
#         "chargepoint": chargepoint
#     }

#     return JsonResponse(data)


# def CustomerToDictionary(chargepoint):
#     """
#     A utility function to convert object of type Blog to a Python Dictionary
#     """
#     output = {}
#     output["id"] = chargepoint.id
#     output["name"] = chargepoint.name
#     output["chargepoint"] = chargepoint.chargepoint
#     output["total_payed"] = chargepoint.total_payed

#     return output

# def customers(request):
#     # Multiple Customers
#     customers = Customer.objects.all()
#     tempCustomers = []

#     for i in range(len(customers)):
#         buffer = CustomerToDictionary(customers[i])
#         buffer["chargepoint"] = ChargepointToDictionary(buffer["chargepoint"])
#         tempCustomers.append(buffer) # Converting `QuerySet` to a Python Dictionary

#     customers = tempCustomers

#     data = {
#         # "customer": customer,
#         "customers": customers
#     }

#     return JsonResponse(data)

# def customers_id(request, id):
#     # Single Customer
#     customer = Customer.objects.get(id = id)

#     # Converting `QuerySet` to a Python Dictionary
#     customer = CustomerToDictionary(customer)
#     customer["chargepoint"] = ChargepointToDictionary(customer["chargepoint"])

#     data = {
#         "customer": customer
#     }

#     return JsonResponse(data)

# def chargepoint_post(request):
#     chargepoints = JSONParser().parse(request)
#     for chargepoint in chargepoints:
#         data = Chargepoint()
#         data.name = chargepoint["name"]
#         data.number_of_chargepoint = chargepoint["number_of_chargepoint"]
#         data.max_power_w = chargepoint["max_power_w"]
#         data.save()
