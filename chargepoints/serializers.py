from rest_framework.serializers import ModelSerializer
 
from chargepoints.models import Chargepoint, Customer
 
class ChargepointSerializer(ModelSerializer):
 
    class Meta:
        model = Chargepoint
        fields = ['id', 'name', 'number_of_chargepoint', 'max_power_w']

class CustomerSerializer(ModelSerializer):
 
    class Meta:
        model = Customer
        fields = ['id', 'name', 'chargepoint', 'total_payed']