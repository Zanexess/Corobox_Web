from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Stuff.models import Stuff
from Stuff.serializers import StuffSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def stuff_list(request):
    if request.method == 'GET':
        stuffs = Stuff.objects.all().filter(owner=request.user)
        serializer = StuffSerializer(stuffs, many=True)
        return JsonResponse(serializer.data, safe=False)