from rest_framework.serializers import ModelSerializer
from firstapp.models import *

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'