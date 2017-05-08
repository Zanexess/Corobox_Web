from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Order.models import Order
from Order.serializers import OrderSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def order_get(request):
    if request.method == 'GET':
        orders = Order.objects.all().filter(owner=request.user).filter(status="PROCESS")
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def order_del(request, uuid):
    # try:
    #     order_obj = Order.objects.get(uuid=uuid)
    # except Exception:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        for order_ob in Order.objects.all():
            order_ob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def order_put(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


