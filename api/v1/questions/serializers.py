
from rest_framework import serializers

from index.models import Questions, ClientEmail


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = '__all__'


class ClientEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientEmail
        fields = '__all__'