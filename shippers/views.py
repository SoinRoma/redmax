from django.views.generic import TemplateView

from index.models import Contact
from order.models import PickupService, DeliveryService


class ShippersView(TemplateView):
    template_name = 'shippers.html'

    def get_context_data(self, **kwargs):
        response = super().get_context_data(**kwargs)
        response["contact"] = Contact.objects.last()
        response['pickup_list'] = PickupService.objects.all()
        response['delivery_list'] = DeliveryService.objects.all()

        return response