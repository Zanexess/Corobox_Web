from rest_framework import serializers
from Corobox import settings
from Address.models import Address


class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    city = serializers.CharField(required=True, allow_blank=False)
    street = serializers.CharField(required=True, allow_blank=False)
    house = serializers.CharField(required=True, allow_blank=False)
    access = serializers.CharField(required=True, allow_blank=False)
    floor = serializers.CharField(required=True, allow_blank=False)
    flat = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('street', instance.street)
        instance.house = validated_data.get('house', instance.house)
        instance.access = validated_data.get('access', instance.access)
        instance.floor = validated_data.get('floor', instance.floor)
        instance.flat = validated_data.get('flat', instance.flat)
        instance.save()
        return instance