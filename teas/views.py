from django.http import JsonResponse
from .models import Tea
from .serializers import TeaSerializer

def tea_list(request):
    teas = Tea.objects.all()
    serializer = TeaSerializer(teas, many=True)
    return JsonResponse({'teas': serializer.data}, safe=False)
