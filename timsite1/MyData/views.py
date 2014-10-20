from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from MyData.serializers import UserSerializer, GroupSerializer, StringParameterSerializer, DataListSerializer, IntegerParameterSerializer, BooleanParameterSerializer, DecimalParameterSerializer, UnitParameterSerializer
from MyData.models import DataList, StringParameter, IntegerParameter, BooleanParameter, DecimalParameter, UnitParameter


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DataListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DataList.objects.all()
    serializer_class = DataListSerializer
	
class StringParameterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = StringParameter.objects.all()
    serializer_class = StringParameterSerializer
		
class IntegerParameterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = IntegerParameter.objects.all()
    serializer_class = IntegerParameterSerializer
		
class BooleanParameterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BooleanParameter.objects.all()
    serializer_class = BooleanParameterSerializer
		
class DecimalParameterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DecimalParameter.objects.all()
    serializer_class = DecimalParameterSerializer
	
class UnitParameterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UnitParameter.objects.all()
    serializer_class = UnitParameterSerializer