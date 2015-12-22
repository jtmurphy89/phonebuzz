# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import durationfield.db.models.fields.duration
import datetime
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwilioCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text=b'Must include international prefix - e.g. +1 555 555 55555', max_length=128)),
                ('time_delay', durationfield.db.models.fields.duration.DurationField(default=datetime.timedelta)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('call_made', models.DateTimeField(null=True, blank=True)),
                ('call_sid', models.CharField(max_length=200, blank=True)),
                ('input', models.CharField(max_length=200, blank=True)),
            ],
        ),
    ]
