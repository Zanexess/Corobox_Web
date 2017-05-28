from rest_framework import serializers
from Corobox import settings
from Categories.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_id = serializers.CharField(required=True)
    image_url = serializers.SerializerMethodField(read_only=True, allow_null=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=120, read_only=True)
    description = serializers.CharField(required=False, allow_blank=True, read_only=True)
    max_weight = serializers.FloatField(read_only=True, required=False)
    monthly_price = serializers.IntegerField(read_only=True, required=False)

    def get_image_url(self, obj):
        return 'http://185.143.172.79:8000/static/' + obj.image_url.url

