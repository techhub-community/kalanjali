from django.shortcuts import render
from .models import PromoSmsModel
from django.http import HttpResponse
import json

sms_text = '''Kalanjali is a Techno-Cultural festival organized every year by Sir M. Visvesvaraya Institute of Technology, Bangalore, where students, artists and performers showcase their talent and skills. So mark your calendars for the 12th and 13th of October.
You can register online on our website http://kalanjali18.in/.
Follow us on  Instagram - Instagram.com/kalanjali_2018 for frequent updates.
For any further queries contact us on:
Rahul Urs - 8197085063
Nishitha - ‭88615 34243'''

# Create your views here.
def promosmsview(request):
    if request.method=="GET":
        return render(request,'promosms/promosms.html')
    if request.method=="POST":
        phone = request.POST['phone']
        if not phone:
            return HttpResponse(json.dumps({"message":"Error (No phone Number)",}),content_type="application/json")
        #send Sms API
        sms_data = PromoSmsModel(
            phone=phone,
            sms_sent=True,
        )
        sms_data.save()
        return HttpResponse(json.dumps({"message":"success",}),content_type="application/json")
    else:
        return render(request,'promosms/promosms.html')
