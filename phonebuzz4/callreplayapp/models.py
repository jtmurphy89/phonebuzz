from django.db import models
from datetime import datetime, timedelta
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from durationfield.db.models.fields.duration import DurationField


class TwilioCall(models.Model):
    phone_number = PhoneNumberField(
        help_text='Must include international prefix - e.g. +1 555 555 55555')
    time_delay = DurationField(default=timedelta)
    created = models.DateTimeField(auto_now_add=True)
    call_made = models.DateTimeField(blank=True, null=True)
    call_sid = models.CharField(max_length=200, blank=True)
    input = models.CharField(max_length=200, blank=True)

    def clean(self):
        """Checks that call is not scheduled before model is created"""
        if self.created + self.time_delay < datetime.now():
            raise ValidationError('Your time interval was less than the minimum allowable time interval.')