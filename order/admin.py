from django.contrib import admin

# Register your models here.
from order.models import PickupService, DeliveryService, Packaging, Order, Receiver

admin.site.register(PickupService)
admin.site.register(DeliveryService)
admin.site.register(Packaging)
admin.site.register(Order)
admin.site.register(Receiver)