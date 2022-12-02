from chargepoints.models import Chargepoint, Customer
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
    queryset = Chargepoint.objects.all()

    def get(self, request, format=None):
        queryset = Chargepoint.objects.all()

        chargepoint_id = self.request.GET.get('chargepoint_id')
        if chargepoint_id is not None:
            queryset = queryset.filter(chargepoint_id=chargepoint_id)
        return queryset

class ChargepointViewsetPost(ModelViewSet):

    serializer_class = ChargepointSerializer
    queryset = Chargepoint.objects.all()

    def post(self, request):
        chargepoint = Chargepoint()
        if request.method == 'POST':
            chargepoint.name = request.POST["name"]
            chargepoint.number_of_chargepoint = request.POST["number_of_chargepoint"]
            chargepoint.max_power_w = request.POST["max_power_w"]
            chargepoint.save()


class ChargepointViewsetDelete(ModelViewSet):

    serializer_class = ChargepointSerializer

    def get_queryset(self):
        queryset = Chargepoint.objects.all()
        chargepoint_id = self.request.GET.get('chargepoint_id')
        if chargepoint_id is not None:
            buffer = queryset.filter(chargepoint_id=chargepoint_id)
            buffer.delete()
        return queryset


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
