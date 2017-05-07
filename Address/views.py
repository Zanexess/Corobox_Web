from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Address.models import Address
from Address.serializers import AddressSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


@csrf_exempt
@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated, ))
def address_get(request):
    if request.method == 'GET':
        addresses = Address.objects.all().filter(owner=request.user)
        serializer = AddressSerializer(addresses, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def address_del(request, pk):
    try:
        address_obj = Address.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        address_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def address_put(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def address_upd(request, pk):
    try:
        address_obj = Address.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressSerializer(address_obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
