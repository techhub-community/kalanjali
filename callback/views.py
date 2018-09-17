from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from . import Checksum
from django.http import HttpResponse
# Create your views here.
@csrf_exempt
def callback(request):
    if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            return render(request,"callback/callback.html",{"paytm":data_dict})
        else:
            return HttpResponse("checksum verification failed!")
    return HttpResponse("INVALID REQUEST",status=200)
