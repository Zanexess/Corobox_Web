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
    uuid = serializers.UUIDField()
    stored_timestamp = TimestampField(read_only=True)
    till = TimestampField(read_only=True)
    paid_till = TimestampField(read_only=True)
    category = CategorySerializer(read_only=True)
    status = serializers.CharField(read_only=True)
    image_url = serializers.SerializerMethodField(allow_null=True)

    def get_image_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.image_url.url
        return request.build_absolute_uri(photo_url)

    class Meta:
        model = Stuff
        fields = ('uuid', 'title', 'description', 'stored_timestamp', 'till', 'paid_till', 'image_url', 'category', 'status')
