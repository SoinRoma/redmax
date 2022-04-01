from django.urls import path
from .views import CreateCallBackView, GetIsAnsweredAPIView

app_name = 'call_back'

urlpatterns = [
    path('create/', CreateCallBackView.as_view(),  name = 'create'),
    path('<int:id>/check_is_answered/', GetIsAnsweredAPIView.as_view(),  name = 'check_is_answered'),

]