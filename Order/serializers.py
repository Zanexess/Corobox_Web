from rest_framework import serializers
from Corobox import settings
from Order.models import Order, CategoryOrder, OrderFrom
from Address.models import Address
from Categories.models import Category
from Categories.serializers import CategorySerializer
from Stuff.models import Stuff
from Stuff.serializers import StuffSerializer
from Address.serializers import AddressSerializer
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TimestampField(serializers.Field):
    def to_representation(self, value):
        epoch = datetime.datetime(1970,1,1)
        return int((value - epoch).total_seconds())

    def to_internal_value(self, data):
        import datetime
        return datetime.datetime.fromtimestamp(int(data))


class CategoryOrderSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = CategoryOrder
        fields = ('category', 'number')


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    created = TimestampField(required=False)
    till = TimestampField(required=True)
    order = CategoryOrderSerializer(many=True, required=True)

    class Meta:
        model = Order
        fields = ('uuid', 'created', 'till', 'address', 'status', 'order')

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
            try:
                category = Category.objects.get(category_id=category_id)
            except Category.DoesNotExist:
                order.delete()
                raise serializers.ValidationError("Category not found")

            categoryOrderObj = CategoryOrder.objects.create(category=category, **order_obj)
            categoryOrderObj.save()
            order.order.add(categoryOrderObj)

        address.owner = order.owner
        address.save()
        return order


class OrderFromSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    created = TimestampField(required=False)
    stuff = StuffSerializer(many=True, required=True)

    class Meta:
        model = Order
        fields = ('uuid', 'created', 'till', 'address', 'status', 'stuff')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        try:
            address = Address.objects.get(**address_data)
        except Address.DoesNotExist:
            address = None

        if not address:
            address = Address.objects.create(**address_data)

        stuff_data = validated_data.pop('stuff')

        order_from = OrderFrom.objects.create(address=address, **validated_data)

        for stuff_obj in stuff_data:
            uuid = stuff_obj.pop('uuid')
            try:
                stuff = Stuff.objects.get(uuid=uuid)
                order_from.stuff.add(stuff)
            except Stuff.DoesNotExist:
                order_from.delete()
                raise serializers.ValidationError("Stuff not found")

        address.owner = order_from.owner
        address.save()
        return order_from


