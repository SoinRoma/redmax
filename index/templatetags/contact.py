from django import template
from index.models import Contact
from order.models import Packaging
register = template.Library()

@register.simple_tag()
def get_last_contact():
    return Contact.objects.last()

@register.simple_tag()
def get_packaging_list():
    return Packaging.objects.all()
