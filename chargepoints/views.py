from chargepoints.models import Chargepoint, Customer
from rest_framework.views import APIView
from rest_framework.response import Response
from chargepoints.serializers import ChargepointSerializer, CustomerSerializer
from rest_framework import status



class ChargepointViewsetGet(APIView):

    def get(self, request, id=None):
        data = Chargepoint.objects.all()
        if id is not None:
            data = data.filter(id=id)
        serializer = ChargepointSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def delete(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ChargepointViewsetPost(APIView):

    def get(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = ChargepointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ChargepointViewsetDelete(APIView):

    def get(self, request, id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, id):
        data = Chargepoint.objects.get(id=id)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CustomerViewsetGet(APIView):

    def get(self, request, id=None):
        data = Customer.objects.all()
        if id is not None:
            data = data.filter(id=id)
        serializer = CustomerSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def delete(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CustomerViewsetPost(APIView):

    def get(self, request, chargepoint_id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, chargepoint_id):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            customer.chargepoint = Chargepoint.objects.get(id=chargepoint_id)
            customer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, chargepoint_id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CustomerViewsetDelete(APIView):

    def get(self, request, id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, id):
        data = Customer.objects.get(id=id)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
