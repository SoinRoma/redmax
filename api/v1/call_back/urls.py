from django.urls import path
from .views import CreateCallBackView

app_name = 'call_back'

urlpatterns = [
    path('create/', CreateCallBackView.as_view(),  name = 'create'),

]