from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Order.models import Order, OrderFrom
from Order.serializers import OrderSerializer, OrderFromSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

# TO

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def order_get(request):
    if request.method == 'GET':
        type = request.GET.get('type')
        if not type:
            orders = Order.objects.all().filter(owner=request.user)
            serializer = OrderSerializer(orders, context={"request": request}, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            orders = Order.objects.all().filter(owner=request.user).filter(status=type)
            serializer = OrderSerializer(orders, context={"request": request}, many=True)
            return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def order_to_del(request, uuid):
    try:
        order_obj = Order.objects.get(uuid=uuid)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        order_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def order_put(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data, context={"request": request})

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def order_upd(request, uuid):
    try:
        order_obj = Order.objects.get(uuid=uuid)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if order_obj.status == 'pending':
            data = JSONParser().parse(request)
            serializer = OrderSerializer(order_obj, data=data, context={"request": request}, partial=True)
            if serializer.is_valid():
                serializer.save(owner=request.user)
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            return Response(status=status.HTTP_409_CONFLICT)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def order_to_cancel(request, uuid):
    try:
        order_obj = Order.objects.get(uuid=uuid)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if order_obj.status == 'pending':
            order_obj.status = 'cancelled'
            order_obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

# FROM

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def order_from_get(request):
    if request.method == 'GET':
        type = request.GET.get('type')
        if not type:
            orders = OrderFrom.objects.all().filter(owner=request.user)
            serializer = OrderFromSerializer(orders, context={"request": request}, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            orders = OrderFrom.objects.all().filter(owner=request.user).filter(status=type)
            serializer = OrderFromSerializer(orders, context={"request": request}, many=True)
            return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def order_from_put(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderFromSerializer(data=data, context={"request": request})

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def order_from_del(request, uuid):
    try:
        order_obj = OrderFrom.objects.get(uuid=uuid)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        order_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def order_from_cancel(request, uuid):
    try:
        order_obj = OrderFrom.objects.get(uuid=uuid)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if order_obj.status == 'pending':

            for stuff in order_obj.stuff.all():
                stuff.status = 'stored'
                stuff.save()
            order_obj.status = 'cancelled'
            order_obj.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------------------------------------------------------------------------------
# METHODS FOR CURRIER
# TO


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def order_to_deliver(request):
    if request.method == 'GET':
        orders = Order.objects.all().filter(Q(status='pending') | Q(status='packaging'))
        serializer = OrderSerializer(orders, context={"request": request}, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def order_to_change_status(request):
    if request.method == 'GET':
        uuid = request.GET.get('uuid')
        type_status = request.GET.get('status')
        if uuid and type_status:
            try:
                order_obj = Order.objects.get(uuid=uuid)
                if type_status == 'delivering' or type_status == 'done':
                    order_obj.status = type_status
                    order_obj.save()
                    return Response({"success": "ok"}, status.HTTP_201_CREATED)
                else:
                    return Response({"error": "incorrect type_status; allowed only delivering or done"},
                                    status.HTTP_404_NOT_FOUND)

            except Order.DoesNotExist:
                return Response({"error": "order not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "uuid or status not found"}, status=status.HTTP_404_NOT_FOUND)


# ------------------------------------------------------------------------------------------------
# FROM


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def order_from_deliver(request):
    if request.method == 'GET':
        orders = OrderFrom.objects.all().filter(Q(status='pending') | Q(status='packaging'))
        serializer = OrderFromSerializer(orders, context={"request": request}, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def order_from_change_status(request):
    if request.method == 'GET':
        uuid = request.GET.get('uuid')
        type_status = request.GET.get('status')
        if uuid and type_status:
            try:
                order_obj = OrderFrom.objects.get(uuid=uuid)
                if type_status == 'delivering' or type_status == 'done':
                    order_obj.status = type_status
                    order_obj.save()
                    return Response({"success": "ok"}, status.HTTP_201_CREATED)
                else:
                    return Response({"error": "incorrect type_status; allowed only delivering or done"},
                                    status.HTTP_404_NOT_FOUND)

            except OrderFrom.DoesNotExist:
                return Response({"error": "order not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "uuid or status not found"}, status=status.HTTP_404_NOT_FOUND)