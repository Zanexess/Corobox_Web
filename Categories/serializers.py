from rest_framework import serializers
from Corobox import settings
from Categories.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image_url = serializers.CharField(read_only=True, allow_null=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=120, read_only=True)
    description = serializers.CharField(required=False, allow_blank=True, read_only=True)
    max_weight = serializers.FloatField(read_only=True)
    monthly_price = serializers.IntegerField(read_only=True)

    def get_image_url(self, obj):
        return obj.image.url