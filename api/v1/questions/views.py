from rest_framework.generics import CreateAPIView

from api.v1.questions.serializers import QuestionsSerializer, ClientEmailSerializer


class CreateQuestionsView(CreateAPIView):
    serializer_class = QuestionsSerializer


class CreateClientEmailView(CreateAPIView):
    serializer_class = ClientEmailSerializer