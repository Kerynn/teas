from django.http import JsonResponse
from .models import Tea
from .models import Customer
from .models import Subscription
from .serializers import TeaSerializer
from .serializers import CustomerSerializer
from .serializers import SubscriptionSerializer
from .serializers import SubscriptionStatusSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def tea_list(request):

    if request.method == 'GET':
        teas = Tea.objects.all()
        serializer = TeaSerializer(teas, many=True)
        return JsonResponse({'teas': serializer.data})

    if request.method == 'POST':
        serializer = TeaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': 'Tea created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def tea_detail(request, id):

    try: 
        tea = Tea.objects.get(pk=id)
    except Tea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeaSerializer(tea)
        return JsonResponse({'tea': serializer.data})

@api_view(['GET', 'POST'])
def customer_list(request):

    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse({'customers': serializer.data})

    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': 'Customer created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def customer_detail(request, id):

    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse({'customer': serializer.data})

@api_view(['GET'])
def customer_subscriptions(request, id):
    
        try:
            customer = Customer.objects.get(pk=id)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        if request.method == 'GET':
            subscriptions = Subscription.objects.filter(customer=customer)
            serializer = SubscriptionSerializer(subscriptions, many=True)
            return JsonResponse({'subscriptions': serializer.data})

@api_view(['GET', 'POST'])
def subscription_list(request):

    if request.method == 'GET':
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return JsonResponse({'subscriptions': serializer.data})

    if request.method == 'POST':
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': 'Subscription created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def subscription_detail(request, id):

    try:
        subscription = Subscription.objects.get(pk=id)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubscriptionSerializer(subscription)
        return JsonResponse({'subscription': serializer.data})
    
    if request.method == 'PUT':
        serializer = SubscriptionStatusSerializer(subscription, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': 'Subscription status updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
