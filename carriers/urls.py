from django.urls import path
from . import views
app_name = 'carriers'

urlpatterns = [
    path('', views.CarriersView.as_view(), name="carrier"),
]
