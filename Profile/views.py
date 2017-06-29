from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Profile.models import User
from Profile.serializers import ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def profile(request):
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = ProfileSerializer(snippets, context={"request": request}, many=True)
        return JsonResponse(serializer.data, safe=False)