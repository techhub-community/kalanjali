from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from . import Checksum
from django.http import HttpResponse
# Create your views here.
@csrf_exempt
def callback(request):
    if request.method == "GET":
        data_dict = {}
        for key in request.GET:
            data_dict[key] = request.GET[key]
        return render(request,"callback/callback.html",{"paytm":data_dict})
    return HttpResponse("INVALID REQUEST",status=200)
