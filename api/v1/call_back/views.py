from rest_framework.generics import CreateAPIView

from api.v1.call_back.serializers import CallBackSerializer


class CreateCallBackView(CreateAPIView):
    serializer_class = CallBackSerializer