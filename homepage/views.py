from django.shortcuts import render
from . import Checksum
import uuid
from instamojo_wrapper import Instamojo
from django.conf import settings

from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

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
