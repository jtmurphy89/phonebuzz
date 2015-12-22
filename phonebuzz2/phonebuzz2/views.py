from django_twilio.decorators import twilio_view
from django_twilio.client import twilio_client
from twilio.twiml import Response
from django.shortcuts import render, redirect
from django.conf import settings


def home(request):
    if request.method == 'POST':
        twilio_client.calls.create(
            to=request.POST['phone_number'],
            from_=settings.TWILIO_NUMBER,
            url=settings.TWILIO_VOICE_URL
        )
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
