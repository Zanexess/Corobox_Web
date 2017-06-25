from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Stuff.models import Stuff
from Stuff.serializers import StuffSerializer
from Order.models import Order
from Categories.models import Category
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def stuff_list(request):
    if request.method == 'GET':
        stuffs = Stuff.objects.all().filter(owner=request.user).filter(status='stored')
        serializer = StuffSerializer(stuffs, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def order_to_stuff(request, uuid):
    if request.method == 'GET':
        try:
            order = Order.objects.get(uuid=uuid)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if order.status == 'pending':
            for category_order in order.order.all():
                category = Category.objects.get(id=category_order.category_id)

                for i in range(1, category_order.number + 1):
                    stuff = Stuff.objects.create(title=category.title,
                                         description='',
                                         till=order.till,
                                         image_url='stuff/bicycle.png',
                                         category=category,
                                         owner=order.owner)
                    stuff.save()

            order.status = "done"
            order.save()
        else:
            return Response(status.HTTP_409_CONFLICT)
    return Response(status=status.HTTP_201_CREATED)

