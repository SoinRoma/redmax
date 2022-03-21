from django.urls import path, include

urlpatterns = [

    path('call_back/', include('api.v1.call_back.urls')),
    path('questions/', include('api.v1.questions.urls'))

]