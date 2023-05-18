from rest_framework import serializers
from .models import Tea, Customer, Subscription

class TeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tea
        fields = ['id', 'name', 'description', 'temperature', 'brew_time']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'address']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'title', 'price', 'status', 'frequency', 'tea', 'customer']

class SubscriptionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['status']