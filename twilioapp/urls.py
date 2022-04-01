from django.urls import path
from . import views
app_name = 'twilio'

urlpatterns = [
    path('handler/', views.TwilioHandlerView.as_view(), name="handler"),
    path('action_handler/', views.TwilioActionHandlerView.as_view(), name="action_handler"),
]