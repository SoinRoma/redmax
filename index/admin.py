from django.contrib import admin
from .models import Contact, Questions, CallBack, ClientEmail, TwilioConfig

admin.site.register(Contact)
admin.site.register(Questions)
admin.site.register(CallBack)
admin.site.register(ClientEmail)
admin.site.register(TwilioConfig)