from django.db import models
from base.models import Base


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