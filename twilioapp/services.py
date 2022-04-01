from django.http import HttpResponse
from twilio.twiml.voice_response import VoiceResponse

from index.models import TwilioConfig, CallBack


class VoiceController:

    def incoming_call_to_main_handle(self, request):  # отвечает авторобот ()
        """Respond to incoming phone calls with a menu of options"""
        # Start our TwiML response
        resp = VoiceResponse()
        config = TwilioConfig.objects.first()
        resp.dial(config.manager_phone)
        return HttpResponse(str(resp), content_type="text/xml")

    def action_handle(self, request):
        resp = VoiceResponse()
        call_status = request.POST.get('CallStatus')
        CallSid = request.POST.get('ParentCallSid')

        if call_status == 'in-progress':
            try:
                cb = CallBack.objects.filter(twilio_call_sid=CallSid).last()
                cb.is_answered = True
                cb.save()
            except:
                print("error")
                pass

        return HttpResponse(str(resp), content_type="text/xml")