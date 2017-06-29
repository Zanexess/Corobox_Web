from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import User
from serializers import ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def profile(request):
    if request.method == 'GET':
        snippets = User.objects.all().filter(id=request.user.id)
        serializer = ProfileSerializer(snippets, context={"request": request}, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def profile_upd(request, pk):
    try:
        user_obj = User.objects.all().filter(id=request.user.id).get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(user_obj, data=data, context={"request": request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)