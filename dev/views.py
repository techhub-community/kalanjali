from django.shortcuts import render

from django.conf import settings

from django.http import HttpResponse,HttpResponseRedirect

from homepage.forms import RegistrationForm
from homepage.models import RegistrationModel
from django.views.decorators.csrf import csrf_exempt
import json

import urllib.request as urlRequest
import urllib.parse

#recaptcha
import urllib
# import urllib2
import json

# Create your views here.

@csrf_exempt
def devview(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        event = request.POST['event_selected']
        email = request.POST['email']
        # add txn_id check here
        if RegistrationModel.objects.filter(txn_id=request.POST['txn_id']):
            return HttpResponse(json.dumps({"message":"Transaction ID is already Registered",}),content_type="application/json")
        if user_form.is_valid():
            recaptcha_response = request.POST['g-recaptcha-response']
            values = {
                'secret' : "6LfhvHIUAAAAALdo3dY_Ztr6yty-rXyJ2GK-Ti7-",
                'response' : recaptcha_response,
            }
            data = urllib.urlencode(values)
            req = urlRequest.Request(url, data)
            response = urlRequest.urlopen(req)
            result = json.load(response)

            if result['success']:
                return HttpResponse("recaptcha Success")
            else:
                return HttpResponse("recaptcha Failed")

            new_data = RegistrationModel(
                number = len(RegistrationModel.objects.all())+1,
                coord_id = user_form.cleaned_data['coord_id'],
                name = user_form.cleaned_data['name'],
                phone = user_form.cleaned_data['phone'],
                email = email,
                college = user_form.cleaned_data['college'],
                year = user_form.cleaned_data['year'],
                event = event,
                txn_id = user_form.cleaned_data['txn_id'],
                amount = user_form.cleaned_data['amount']
            )
            new_data.save()
    elif request.method == "GET":
        return HttpResponseRedirect("/admin")
