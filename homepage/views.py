from django.shortcuts import render
from . import Checksum
import uuid
from instamojo_wrapper import Instamojo
from django.conf import settings

from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage

from .forms import RegistrationForm
from .models import RegistrationModel
from django.views.decorators.csrf import csrf_exempt
import json

from django.template.loader import render_to_string

# Create your views here.

import urllib.request as urlRequest
import urllib.parse

def sendSMS(apikey, numbers, sender, message):
    params = {'apikey': apikey, 'numbers': numbers, 'message' : message, 'sender': sender}
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
        + urllib.parse.urlencode(params))
    return (f.read(), f.code)

def sendEmail(email,event,name,phone,college,year,txn_id,amount):
    html_template=render_to_string("homepage/email.html", {"user": dict(event=event,name=name,email=email,phone=phone,college=college,year=year,txn_id=txn_id,amount=amount)})
    msg = EmailMessage("Registration successful!",html_template,"no-reply@kalanjali18.in",[email,])
    msg.content_subtype = "html"
    check = msg.send()
    if check!=1:
        email_error_file = open('logs/email_error_log.log','a')
        email_error_file.write("Error For Email : {0}\terror code:{1}".format(email,str(check)))
        email_error_file.close()

@csrf_exempt
def register(request):
    if request.method == "GET":
        return HttpResponseRedirect("/admin")
    elif request.method == "POST":
        user_form = RegistrationForm(request.POST)
        event = request.POST['event_selected']
        email = request.POST['email']
        if 'g-recaptcha-response' not in request.POST.keys() or request.POST['g-recaptcha-response'] == '':
            return HttpResponse(json.dumps({"message":"Captcha Verification Failed!",}),content_type="application/json")
        # add txn_id check here
        if RegistrationModel.objects.filter(txn_id=request.POST['txn_id']):
            return HttpResponse(json.dumps({"message":"Transaction ID is already Registered",}),content_type="application/json")
        if user_form.is_valid():
            recaptcha_response = request.POST['g-recaptcha-response']
            values = {
                'secret' : "6LfhvHIUAAAAALdo3dY_Ztr6yty-rXyJ2GK-Ti7-", #FINAL key
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
                #send Email
                sendEmail(email,event,name=user_form.cleaned_data['name'],phone=user_form.cleaned_data['phone'],college=user_form.cleaned_data['college'],year=user_form.cleaned_data['year'],txn_id=user_form.cleaned_data['txn_id'],amount=user_form.cleaned_data['amount'])
                return HttpResponse(json.dumps({"message":"Registration Successful. Kindly expect an email from us and see you at Kalanjali 2019.",}),content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message":"There is some ERROR in the filled Form", "data": json.dumps(result) }),content_type="application/json")
        elif request.POST['coord_id'] == '':
            return HttpResponse(json.dumps({"message":"No Coordinator ID",}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message":"There is some ERROR in the filled Form",}),content_type="application/json")

	# elif request.method == "POST":
	# 	resp, code = sendSMS(apikey='aJOo8nc0mC4-QKjRBPhSt4aFSQBgcXLhgBV7UQdwVY',numbers='91'+request.POST['phone'],message=request.POST['message'],sender='')
	# 	return HttpResponse(str(resp)+'\n'+str(code))



    # def homepage(request):
    #
    # 	server_dict = {
    # 	"amount" : "50",
    # 	"redirect_url" : 'http://206.189.133.171/callback/',
    # 	}
    #
    # 	if request.method == "POST":
    # 		posted = request.POST
    # 		#validate The form here
    # 		#generate key here
    # 		api = Instamojo(
    # 			api_key=settings.IMOJO_API_KEY,
    # 			auth_token=settings.IMOJO_AUTH_TOKEN,
    # 			endpoint=settings.IMOJO_ENDPOINT,
    # 			)
    # 		response = api.payment_request_create(
    # 			buyer_name = posted['buyer_name'],
    # 			email = posted['email'],
    # 			phone = posted['phone'],
    # 			purpose = posted['purpose'],
    # 			amount = server_dict['amount'],
    # 			redirect_url = server_dict['redirect_url'],
    # 		)
    # 		#check if successfull and redirect accordingly
    # 		if response['success']:
    # 			print("\n\nsuccess\n"+response['payment_request']['longurl'])
    # 			return HttpResponseRedirect(response['payment_request']['longurl'])
    # 		else:
    # 			return HttpResponse(response['message'])
    # 	else:
    # 		user_dict = {
    # 		"buyer_name" : "Rahul Jaiswal",
    # 		"email" : "itsauselessid@gmail.com",
    # 		"phone" : "9916743175",
    # 		"purpose" : "Testing",
    # 		}
    # 		return render(request,"homepage/index.html",{'form_dict':user_dict})
    # @csrf_exempt
    # def msg_api(request):
    # 	if request.method == "GET":
    # 		return render(request,"homepage/index.html",{'form':RegistrationForm})
    # 	elif request.method == "POST":
    # 		user_form = RegistrationForm(request.POST)
    # 		if user_form.is_valid():
    # 			new_data = RegistrionModel(
    # 								name = user_form.cleaned_data['name'],
    # 								phone = user_form.cleaned_data['phone'],
    # 								email = user_form.cleaned_data['email'],
    # 								college = user_form.cleaned_data['college'],
    # 								branch = user_form.cleaned_data['branch'],
    # 								semester = user_form.cleaned_data['semester'],
    # 								event = user_form.cleaned_data['event_selected'],
    # 								txn_id = user_form.cleaned_data['txn_id'],
    # 			)
    # 			new_data.save()
    # 			send_mail("Registration successful",
    # 			"You have Registered for event :{0}".format(user_form.cleaned_data['event']),
    # 			"noreply@kalanjali18.in",
    # 			user_form.cleaned_data['email'],
    # 			)
    # 			print(request.POST)
    # 			return HttpResponse("DONE")
    # 		else:
    # 			return HttpResponse("Error")
