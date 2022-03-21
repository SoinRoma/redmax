
from django.views.generic import TemplateView
from index.models import Contact

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        response = super().get_context_data(**kwargs)
        response["contact"] = Contact.objects.last()

        return response
