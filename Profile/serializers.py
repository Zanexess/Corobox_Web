from rest_framework import serializers
from models import User
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


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone', 'email')