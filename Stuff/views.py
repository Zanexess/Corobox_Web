from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Stuff.models import Stuff
from Stuff.serializers import StuffSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def stuff_list(request):
    if request.method == 'GET':
        snippets = Stuff.objects.all().filter(owner=request.user)
        serializer = StuffSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)