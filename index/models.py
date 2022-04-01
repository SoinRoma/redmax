from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Dial, Number

from base.models import Base
from main.settings import TWILIO_ACCOUNT_SID, TWILIO_TOKEN, TWILIO_CALLER_ID


class TwilioConfig(models.Model):
    manager_phone = models.CharField(max_length=255, null=True, blank=True)
    caller_phone = models.CharField(max_length=255, null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(Base):
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    hr_link = models.URLField(null=True, blank=True)
    ios_app = models.URLField(null=True, blank=True)
    android_app = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.phone} | {self.id}"


class CallBack(Base):
    phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    is_answered = models.BooleanField(default=False)
    twilio_call_sid = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"{self.phone} | {self.id}"


class Questions(Base):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    question = models.TextField()

    def __str__(self):
        return f"{self.phone} | {self.name}"


class ClientEmail(Base):
    email = models.EmailField()

    def __str__(self):
        return f"{self.id} | {self.email}"


@receiver(post_save, sender=CallBack)
def call_manager(sender, instance, created, **kwargs):
    if created:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_TOKEN)
        resp = VoiceResponse()
        config = TwilioConfig.objects.first()
        resp.say(config.text, language="ru-RU")
        dial = Dial(record='record-from-answer',
                    timeout=10,
                    method='POST')
        dial.number(phone_number=config.manager_phone, status_callback_event='answered', status_callback='https://7ad0-213-230-112-46.ngrok.io/twilio/action_handler/', status_callback_method='POST')
        resp.append(dial)


        if config.caller_phone:
            call = client.calls.create(from_=config.caller_phone, to=instance.phone, twiml=str(resp))
        else:
            call = client.calls.create(from_=TWILIO_CALLER_ID, to=instance.phone, twiml=str(resp))
        instance.twilio_call_sid = call.sid
        instance.save()