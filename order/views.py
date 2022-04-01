from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from order.models import Order
from order.serializers import OrderSerializer


class OrderCreate(CreateAPIView):
    model = Order
    serializer_class = OrderSerializer


