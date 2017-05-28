from rest_framework import serializers
from Corobox import settings
from Order.models import Order, CategoryOrder
from Address.models import Address
from Categories.models import Category
from Categories.serializers import CategorySerializer
from Address.serializers import AddressSerializer
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TimestampField(serializers.Field):
    def to_representation(self, value):
        epoch = datetime.datetime(1970,1,1)
        return int((value - epoch).total_seconds())


class CategoryOrderSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = CategoryOrder
        fields = ('category', 'number')


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    created = TimestampField(required=False)
    order = CategoryOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ('uuid', 'created', 'address', 'status', 'order')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        try:
            address = Address.objects.get(**address_data)
        except Address.DoesNotExist:
            address = None

        if not address:
            address = Address.objects.create(**address_data)

        order_data = validated_data.pop("order")

        order = Order.objects.create(address=address, **validated_data)

        for order_obj in order_data:
            category_data = order_obj.pop('category')
            category_id = category_data.pop('category_id')
            category = Category.objects.get(category_id=category_id)

            categoryOrderObj = CategoryOrder.objects.create(category=category, **order_obj)
            categoryOrderObj.save()
            order.order.add(categoryOrderObj)

        address.owner = order.owner
        address.save()
        return order