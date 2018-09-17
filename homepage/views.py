from django.shortcuts import render
from . import Checksum
import uuid
from django.conf import settings
# Create your views here.

def homepage(request):
	# MERCHANT_KEY = "RwH39SZTZUpQbJCY"
	# MERCHANT_ID = "NONESt79835244795367"
	# CALLBACK_URL ='http://206.189.133.171/callback/'
	PAYTM_ORDER_ID = str(uuid.uuid4())
	PAYTM_CUST_ID = str(uuid.uuid4())
	bill_amount = 2
	if bill_amount:
		data_dict = {
		'MID':settings.PAYTM_MERCHANT_ID,
		"ORDER_ID":PAYTM_ORDER_ID,
		"CUST_ID":PAYTM_CUST_ID,
		'TXN_AMOUNT':str(bill_amount),
		'INDUSTRY_TYPE_ID':settings.PAYTM_INDUSTRY_TYPE_ID,
		'WEBSITE':settings.PAYTM_WEBSITE,
		'CHANNEL_ID':settings.PAYTM_CHANNEL_ID,
		'CALLBACK_URL':settings.PAYTM_CALLBACK_URL,
		}
		param_dict = data_dict
		param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, settings.PAYTM_MERCHANT_KEY)
		return render(request,"homepage/index.html",{'paytmdict':param_dict})
	else:
		return HttpResponse("Bill Amount Could not find. ?bill_amount=2")
