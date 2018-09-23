from django.shortcuts import render
from . import Checksum
import uuid
from instamojo_wrapper import Instamojo
from django.conf import settings

from django.http import HttpResponse,HttpResponseRedirect

from .forms import RegistrationForm
from .models import RegistrationModel
# Create your views here.
#
import urllib.request
import urllib.parse

def sendSMS(apikey, numbers, sender, message):
    params = {'apikey': apikey, 'numbers': numbers, 'message' : message, 'sender': sender}
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
        + urllib.parse.urlencode(params))
    return (f.read(), f.code)

def homepage(request):

	server_dict = {
	"amount" : "50",
	"redirect_url" : 'http://206.189.133.171/callback/',
	}

	if request.method == "POST":
		posted = request.POST
		#validate The form here
		#generate key here
		api = Instamojo(
			api_key=settings.IMOJO_API_KEY,
			auth_token=settings.IMOJO_AUTH_TOKEN,
			endpoint=settings.IMOJO_ENDPOINT,
			)
		response = api.payment_request_create(
			buyer_name = posted['buyer_name'],
			email = posted['email'],
			phone = posted['phone'],
			purpose = posted['purpose'],
			amount = server_dict['amount'],
			redirect_url = server_dict['redirect_url'],
		)
		#check if successfull and redirect accordingly
		if response['success']:
			print("\n\nsuccess\n"+response['payment_request']['longurl'])
			return HttpResponseRedirect(response['payment_request']['longurl'])
		else:
			return HttpResponse(response['message'])
	else:
		user_dict = {
		"buyer_name" : "Rahul Jaiswal",
		"email" : "itsauselessid@gmail.com",
		"phone" : "9916743175",
		"purpose" : "Testing",
		}
		return render(request,"homepage/index.html",{'form_dict':user_dict})

def msg_api(request):
	if request.method == "GET":
		return render(request,"homepage/index.html",{'form':RegistrationForm})
	elif request.method == "POST":
		user_form = RegistrationForm(request.POST)
		if user_form.is_valid():
			new_data = RegistrationModel(
								first_name = user_form.cleaned_data['first_name'],
								last_name = user_form.cleaned_data['last_name'],
								phone = user_form.cleaned_data['phone'],
								email = user_form.cleaned_data['email'],
								college = user_form.cleaned_data['college'],
								branch = user_form.cleaned_data['branch'],
								semester = user_form.cleaned_data['semester'],
								event = user_form.cleaned_data['event_selected'],
								txn_id = user_form.cleaned_data['txn_id'],
			)
			new_data.save()
			print(request.POST)
			return HttpResponse("DONE")
		else:
			return HttpResponse("Error")

	# elif request.method == "POST":
	# 	resp, code = sendSMS(apikey='aJOo8nc0mC4-QKjRBPhSt4aFSQBgcXLhgBV7UQdwVY',numbers='91'+request.POST['phone'],message=request.POST['message'],sender='')
	# 	return HttpResponse(str(resp)+'\n'+str(code))
