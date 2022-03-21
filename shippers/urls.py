from django.urls import path
from . import views
app_name = 'shippers'

urlpatterns = [
    path('', views.ShippersView.as_view(), name="shipper"),
]