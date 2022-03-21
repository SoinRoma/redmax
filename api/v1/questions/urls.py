from django.urls import path
from .views import CreateQuestionsView, CreateClientEmailView

app_name = 'questions'

urlpatterns = [
    path('create/', CreateQuestionsView.as_view(),  name = 'create'),
    path('create/email/', CreateClientEmailView.as_view(),  name = 'create_email'),

]