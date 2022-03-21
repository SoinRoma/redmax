from django.urls import path
from . import views
app_name = 'brokers'

urlpatterns = [
    path('', views.BrokersView.as_view(), name="broker"),
]
