from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from firstapp.models import *
from firstapp.serializers import *
# Create your views here.

class AddressViewSets(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class CompanyViewSets(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
