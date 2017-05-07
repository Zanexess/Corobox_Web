from rest_framework import serializers
from Corobox import settings
from Address.models import Address


class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    street = serializers.CharField(required=True, allow_blank=False)
    house = serializers.CharField(required=True, allow_blank=False)
    access = serializers.CharField(required=True, allow_blank=False)
    floor = serializers.CharField(required=True, allow_blank=False)
    flat = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

