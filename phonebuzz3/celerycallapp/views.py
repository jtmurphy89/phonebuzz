from .models import TwilioCall
from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from django.shortcuts import render, redirect
from .tasks import make_twilio_call


def home(request):
    if request.method == 'POST':
        # use celery to queue the phonebuzz call in the background so the server doesn't hang
        twilio_call = TwilioCall(
            phone_number=request.POST['phone_number'],
            time_delay=request.POST['time_delay_field']
        )
        twilio_call.save()
        phone_number = str(twilio_call.phone_number)
        call_time = twilio_call.created + twilio_call.time_delay
        make_twilio_call.apply_async((phone_number,), eta=call_time)
        return redirect('/')
    return render(request, 'home.html')


@twilio_view
def voice(request):
    r = Response()
    with r.gather(action='/respond/') as g:
        g.say('Please enter a number to play phone buzz. Press the pound key when finished.', voice='woman')
        g.pause(length=10)
    return r


@twilio_view
def respond(request):
    digits = request.POST.get('Digits', '')
    r = Response()
    if digits == '':
        r.say('No number was entered.', voice='woman')
    else:
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