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
                'secret' : "6LcIvnIUAAAAAJumlie4zUhQy4y7I20ufzCvOrxF", #ABHI's key
                'response' : recaptcha_response,
            }
            data = urllib.parse.urlencode(values)
            data = data.encode('utf-8')
            apiurl = "https://www.google.com/recaptcha/api/siteverify"
            req = urlRequest.Request(apiurl, data)
            response = urlRequest.urlopen(req)
            result = json.load(response)
            if result['success']:
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
                sendEmail(email,event,name=user_form.cleaned_data['name'],phone=user_form.cleaned_data['phone'],college=user_form.cleaned_data['college'],year=user_form.cleaned_data['year'],txn_id=user_form.cleaned_data['txn_id'],amount=user_form.cleaned_data['amount'])
                return HttpResponse(json.dumps({"message":"success",}),content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message":"reCaptcha Verification Failed!",}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message":"Please re-check the details entered",}),content_type="application/json")
    elif request.method == "GET":
        return render(request,'dev/recaptcha.html')
