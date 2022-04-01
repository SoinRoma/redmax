from rest_framework.serializers import ModelSerializer
from django.core.mail import EmailMessage, mail_admins
from order.models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'




