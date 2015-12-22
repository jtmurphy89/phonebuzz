from __future__ import absolute_import
from celery import shared_task
from .models import TwilioCall
from django_twilio.client import twilio_client
from datetime import datetime


@shared_task
def make_twilio_call(twilio_call_id, twilio_number, call_url):
    twilio_call = TwilioCall.objects.get(pk=twilio_call_id)
    twilio_call.call_made = datetime.now()

    call = twilio_client.calls.create(
        to=str(twilio_call.phone_number),
        from_=twilio_number,
        url=call_url
    )
    twilio_call.call_sid = call.sid
    twilio_call.save()