from .models import TwilioCall
from django.conf import settings
from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from django.shortcuts import render, redirect
from .tasks import make_twilio_call


def home(request):
    if request.method == 'POST':
        twilio_call = TwilioCall(
            phone_number=request.POST['phone_number'],
            time_delay=request.POST['time_delay_field']
        )
        twilio_call.save()
        call_url = settings.TWILIO_VOICE_URL
        call_time = twilio_call.created + twilio_call.time_delay
        make_twilio_call.apply_async(args=[twilio_call.pk, settings.TWILIO_NUMBER, call_url], eta=call_time)
        return redirect('/')
    call_history = TwilioCall.objects.exclude(input=u'')
    return render(request, 'home.html', {'call_history': call_history})


@twilio_view
def voice(request):
    r = Response()
    with r.gather(action='/respond/') as g:
        g.say('Please enter a number to play phone buzz. Press the pound key when finished.', voice='woman')
        g.pause(length=10)
    return r


@twilio_view
def respond(request):
    digits = request.POST['Digits']
    sid = request.POST['CallSid']
    twilio_call = TwilioCall.objects.get(call_sid=sid)
    twilio_call.input = digits
    twilio_call.save()
    return redirect('read', digits=digits)


@twilio_view
def replay(request, pk):
    twilio_call = TwilioCall.objects.get(pk=pk)
    input = twilio_call.input + '/'
    replay_call = TwilioCall(
        phone_number=twilio_call.phone_number,
        input=twilio_call.input
    )
    replay_call.save()
    call_url = settings.TWILIO_REPLAY_URL + input
    make_twilio_call.apply_async((replay_call.pk, settings.TWILIO_NUMBER, call_url,))
    return redirect('home')


@twilio_view
def read(request, digits):
    r = Response()
    d = int(digits) + 1
    pbuzz = ""
    for i in range(1, d):
        if i % 3 == 0 and i % 5 != 0:
            pbuzz += "Fizz, "
        elif i % 5 == 0 and i % 3 != 0:
            pbuzz += "Buzz, "
        elif i % 3 == 0 and i % 5 == 0:
            pbuzz += "Fizz Buzz, "
        else:
            pbuzz += str(i) + ", "
    r.say(pbuzz[:-2], voice='woman')
    return r
