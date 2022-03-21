from django.views.generic import TemplateView

from index.models import Contact


class ShippersView(TemplateView):
    template_name = 'shippers.html'

    def get_context_data(self, **kwargs):
        response = super().get_context_data(**kwargs)
        response["contact"] = Contact.objects.last()

        return response