from rest_framework import serializers
from Corobox import settings
from Categories.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=120)
    description = serializers.CharField(required=False, allow_blank=True)
    max_weight = serializers.FloatField()
    monthly_price = serializers.IntegerField()

    def get_image_url(self, obj):
        return obj.image.url