
from rest_framework import serializers

from index.models import CallBack


class CallBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallBack
        fields = '__all__'
