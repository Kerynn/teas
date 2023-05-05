from django.http import JsonResponse
from .models import Tea
from .models import Customer
from .serializers import TeaSerializer
from .serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def tea_list(request):
    teas = Tea.objects.all()
    serializer = TeaSerializer(teas, many=True)
    return JsonResponse({'teas': serializer.data})

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
