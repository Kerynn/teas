from django.http import JsonResponse
from .models import Tea
from .models import Customer
from .serializers import TeaSerializer
from .serializers import CustomerSerializer

def tea_list(request):
    teas = Tea.objects.all()
    serializer = TeaSerializer(teas, many=True)
    return JsonResponse({'teas': serializer.data})

def customer_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return JsonResponse({'customers': serializer.data})
