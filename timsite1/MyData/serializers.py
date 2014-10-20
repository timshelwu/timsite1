from django.contrib.auth.models import User, Group
from rest_framework import serializers
from MyData.models import DataList, StringParameter, IntegerParameter, BooleanParameter, DecimalParameter, UnitParameter


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class DataListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataList
        fields = (['name']) #'myParent'
		
class StringParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StringParameter
        fields = ('name', 'value') #'myParent'
		
class IntegerParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntegerParameter
        fields = ('name', 'value') #'myParent'
		
class BooleanParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BooleanParameter
        fields = ('name', 'value') #'myParent'
		
class DecimalParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DecimalParameter
        fields = ('name', 'value') #'myParent'

class UnitParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnitParameter
        fields = (['name']) #'myParent'