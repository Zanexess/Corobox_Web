from rest_framework import serializers
from Corobox import settings
from Order.models import Order
from Address.models import Address
from Address.serializers import AddressSerializer
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TimestampField(serializers.Field):
    def to_representation(self, value):
        epoch = datetime.datetime(1970,1,1)
        return int((value - epoch).total_seconds())


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    created = TimestampField(required=False)

    class Meta:
        model = Order
        fields = ('uuid', 'created', 'address', 'status')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        try:
            address = Address.objects.get(**address_data)
        except Address.DoesNotExist:
            address = None

        if not address:
            address = Address.objects.create(**address_data)
        order = Order.objects.create(address=address, **validated_data)
        address.owner = order.owner
        address.save()
        return order

    # def create(self, validated_data):
    #     address = validated_data.pop('address', None)
    #     if not address:
    #         return None
    #
    #     order = Order.objects.create(**validated_data)
    #     address, created = AddressSerializer(address) Address.objects.get_or_create(id=address['id'], defaults=address)
    #     validated_data['address'] = address
    #     order.address = address
    #
    #     if not order.address:
    #         return None
    #     else:
    #         return order

    # def update_or_create_address(self, validated_data):
    #     data = validated_data.pop('address', None)
    #     if not data:
    #         return None
    #
    #     address, created = Address.objects.update_or_create(
    #         id=data.pop('id'), defaults=data)
    #
    #     validated_data['address'] = address
    #
    # def create(self, validated_data):
    #     self.update_or_create_address(validated_data)
    #     return super(OrderSerializer, self).create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     self.update_or_create_address(validated_data)
    #     return super(OrderSerializer, self).update(instance, validated_data)