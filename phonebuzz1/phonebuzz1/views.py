from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from django.http import HttpResponseRedirect


@twilio_view
def voice(request):
    """Create a Twilio response object which gathers the callers input"""
    r = Response()
    with r.gather(action='/respond/') as g:
        g.say('Please enter a number to play phone buzz. Press the pound key when finished.', voice='woman')
        g.pause(length=10)
    return r


@twilio_view
def respond(request):
    """Gets digits collected by Gather verb and reads back the fizzbuzz output"""
    digits = request.POST.get('Digits', '')
    r = Response()
    if digits == '':
        r.say('No number was entered.', voice='woman')
        return HttpResponseRedirect('/voice/')
    else:
        d = int(digits)
        pbuzz = ""
        for i in range(1,d+1):
            if i % 3 == 0 and i % 5 != 0:
                pbuzz += "Fizz, "
            elif i % 5 == 0 and i % 3 != 0:
                pbuzz += "Buzz, "
            elif i% 3 == 0 and i % 5 == 0:
                pbuzz += "Fizz Buzz, "
            else:
                pbuzz += str(i) + ", "
        r.say(pbuzz[:-2], voice='woman')
    return r