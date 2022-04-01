from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView

from twilioapp.services import VoiceController


class TwilioHandlerView(APIView):
    def post(self, request, *args, **kwargs):
        voice_controller = VoiceController()
        return voice_controller.incoming_call_to_main_handle(request)

class TwilioActionHandlerView(APIView):
    def post(self, request, *args, **kwargs):
        voice_controller = VoiceController()
        return voice_controller.action_handle(request)