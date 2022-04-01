import re

import requests
from django.core.mail import send_mail
from django.db import models

# Create your models here.
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your models here.
class PickupService(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DeliveryService(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Packaging(models.Model):
    name = models.CharField(max_length=255)
    length = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    address_from = models.CharField(max_length=255, null=True, blank=True)
    address_to = models.CharField(max_length=255, null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    pickup = models.ForeignKey(PickupService, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.ManyToManyField(DeliveryService, blank=True)
    length = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    loading_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    page_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.name}"

    def get_delivery_list_string(self):
        delivery_list = ''
        for delivery in self.delivery.all():
            delivery_list += f'{delivery.name}; '
        return delivery_list



class Receiver(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email



@receiver(m2m_changed, sender=Order.delivery.through)
def cost_email(sender, instance, action, **kwargs):
    if action == "post_add":
        sender = 'contact@cnulogistics.com'
        subject = 'REDMAX delivery quote'


        try:
            if instance.address_from and instance.address_to and instance.pickup:
                zip_from = re.findall('\d+', instance.address_from)
                zip_to = re.findall('\d+', instance.address_to)
                if zip_from and zip_to:
                    body = {
                        "jsonrpc": "2.0",
                        "method": "getPrice",
                        "params": {
                            "fromZip": zip_from[0],
                            "toZip": zip_to[0],
                            "type": instance.pickup.name.upper()
                        },
                        "id": 1
                    }
                    resp = requests.post(url="https://cnu.cargoetl.com/jsonrpc/map", json=body).json()

                    if resp.get('result'):
                        instance.cost = resp['result'] * 2
                        Order.objects.filter(id=instance.id).update(cost=instance.cost)
        except Exception as e:
            print("error:", e)

        # -------------------------client send (without page_url)
        context = {
            'name': instance.name,
            'cost': instance.cost

        }
        html_message = render_to_string('mail/cost_email.html', context)
        plain_message = strip_tags(html_message)
        send_mail(subject=subject,
                  message=plain_message,
                  html_message=html_message,
                  from_email=sender,
                  recipient_list=[instance.email],
                  fail_silently=False)

        # ------------------------- admin send (with page_url)

        context = {
            'order': instance,
            'delivery_list': instance.get_delivery_list_string(),
            'description': instance.description
        }
        html_message = render_to_string('mail/cost_email_toadmin.html', context)
        plain_message = strip_tags(html_message)

        for mail_receiver in Receiver.objects.all():
            send_mail(subject=subject,
                      message=plain_message,
                      html_message=html_message,
                      from_email=sender,
                      recipient_list=[mail_receiver.email],
                      fail_silently=False)
