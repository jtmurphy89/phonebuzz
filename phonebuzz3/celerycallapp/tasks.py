from __future__ import absolute_import
from celery import shared_task
from django_twilio.client import twilio_client
from django.conf import settings


@shared_task
def make_twilio_call(call_number):
    twilio_client.calls.create(
        to=call_number,
        from_=settings.TWILIO_NUMBER,
        url=settings.TWILIO_VOICE_URL
    )