from rest_framework import serializers
from Corobox import settings
from Address.models import Address


class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    city = serializers.CharField(required=True, allow_blank=False)
    address = serializers.CharField(required=True, allow_blank=False)
    access = serializers.CharField(required=True, allow_blank=False)
    floor = serializers.CharField(required=True, allow_blank=False)
    flat = serializers.CharField(required=True, allow_blank=False)
    useAsDefault = serializers.BooleanField(required=False)

    def create(self, validated_data):
        request = self.context.get('request')
        for address in Address.objects.all().filter(owner=request.user).filter(useAsDefault=True):
            address.useAsDefault = False
            address.save()
        add = Address.objects.create(**validated_data)
        add.useAsDefault = True
        add.save()
        return add

    def update(self, instance, validated_data):
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('address', instance.address)
        instance.access = validated_data.get('access', instance.access)
        instance.floor = validated_data.get('floor', instance.floor)
        instance.flat = validated_data.get('flat', instance.flat)
        instance.address = validated_data.get("useAsDefault", instance.useAsDefault)
        instance.save()
        return instance