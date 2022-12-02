from chargepoints.models import Chargepoint, Customer
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from chargepoints.serializers import ChargepointSerializer, CustomerSerializer
from rest_framework import status


class ChargepointAPIView(APIView):
 
    def get(self, *args, **kwargs):
        chargepoints = Chargepoint.objects.all()
        serializer = ChargepointSerializer(chargepoints, many=True)
        return Response(serializer.data)

class ChargepointViewsetGet(APIView):

    def get(self, request):
        chargepoint_id = self.request.GET.get('chargepoint_id')
        data = Chargepoint.objects.all()
        if chargepoint_id is not None:
            data = data.filter(chargepoint_id=chargepoint_id)
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

    def delete(self, request, id):
        data = Chargepoint.objects.get(id=id)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerAPIView(APIView):
 
    def get(self, *args, **kwargs):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class CustomerViewsetPost(ModelViewSet):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class CustomerViewsetGet(ReadOnlyModelViewSet):

    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()

        customer_id = self.request.GET.get('customer_id')
        if customer_id is not None:
            queryset = queryset.filter(customer_id=customer_id)
        return queryset

class CustomerViewsetDelete(ModelViewSet):

    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        customer_id = self.request.GET.get('customer_id')
        if customer_id is not None:
            buffer = queryset.filter(customer_id=customer_id)
            buffer.delete()
        return queryset
