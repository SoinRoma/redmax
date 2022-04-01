from django.http import JsonResponse, Http404
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from index.models import CallBack

from api.v1.call_back.serializers import CallBackSerializer


class CreateCallBackView(CreateAPIView):
    serializer_class = CallBackSerializer

class GetIsAnsweredAPIView(APIView):
    def get(self, *args, **kwargs):
        try:
            is_answered = CallBack.objects.get(id=self.kwargs.get('id')).is_answered
            return JsonResponse({'is_answered':is_answered}, status=200)
        except:
            raise Http404("CallBack not found")