from rest_framework import serializers
from Corobox import settings
from Stuff.models import Stuff
from Categories.serializers import CategorySerializer
from Categories.models import Category
import datetime


class TimestampField(serializers.Field):
    def to_representation(self, value):
        epoch = datetime.datetime(1970,1,1)
        return int((value - epoch).total_seconds())

    def to_internal_value(self, data):
        import datetime
        return datetime.datetime.fromtimestamp(int(data))


class StuffSerializer(serializers.ModelSerializer):
    stored_timestamp = TimestampField(required=True)
    till = TimestampField(required=True)
    category = CategorySerializer()
    image_url = serializers.SerializerMethodField(allow_null=True)

    def get_image_url(self, obj):
        return 'http://185.143.172.79:8000/static/' + obj.image_url.url

    class Meta:
        model = Stuff
        fields = ('uuid', 'title', 'description', 'stored_timestamp', 'till', 'image_url', 'category')
