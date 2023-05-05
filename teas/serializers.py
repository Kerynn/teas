from rest_framework import serializers
from .models import Tea
from .models import Customer

class TeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tea
        fields = ['id', 'name', 'description', 'temperature', 'brew_time']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'address']