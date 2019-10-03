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
# Create your views here.

import urllib.request as urlRequest
import urllib.parse

def sendSMS(apikey, numbers, sender, message):
    params = {'apikey': apikey, 'numbers': numbers, 'message' : message, 'sender': sender}
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
        + urllib.parse.urlencode(params))
    return (f.read(), f.code)

def sendEmail(email,event,name,phone,college,year,txn_id,amount):
    html_template = '''


    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
    	<!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
    	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    	<meta name="viewport" content="width=device-width">
    	<!--[if !mso]><!-->
    	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    	<!--<![endif]-->
    	<title></title>
    	<!--[if !mso]><!-->
    	<link href="https://fonts.googleapis.com/css?family=Oxygen" rel="stylesheet" type="text/css">
    	<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
    	<!--<![endif]-->
    	<style type="text/css">
    		body {
    			margin: 0;
    			padding: 0;
    		}

    		table,
    		td,
    		tr {
    			vertical-align: top;
    			border-collapse: collapse;
    		}

    		* {
    			line-height: inherit;
    		}

    		a[x-apple-data-detectors=true] {
    			color: inherit !important;
    			text-decoration: none !important;
    		}
    	</style>
    	<style type="text/css" id="media-query">
    		@media (max-width: 670px) {

    			.block-grid,
    			.col {
    				min-width: 320px !important;
    				max-width: 100% !important;
    				display: block !important;
    			}

    			.block-grid {
    				width: 100% !important;
    			}

    			.col {
    				width: 100% !important;
    			}

    			.col>div {
    				margin: 0 auto;
    			}

    			img.fullwidth,
    			img.fullwidthOnMobile {
    				max-width: 100% !important;
    			}

    			.no-stack .col {
    				min-width: 0 !important;
    				display: table-cell !important;
    			}

    			.no-stack.two-up .col {
    				width: 50% !important;
    			}

    			.no-stack .col.num4 {
    				width: 33% !important;
    			}

    			.no-stack .col.num8 {
    				width: 66% !important;
    			}

    			.no-stack .col.num4 {
    				width: 33% !important;
    			}

    			.no-stack .col.num3 {
    				width: 25% !important;
    			}

    			.no-stack .col.num6 {
    				width: 50% !important;
    			}

    			.no-stack .col.num9 {
    				width: 75% !important;
    			}

    			.video-block {
    				max-width: none !important;
    			}

    			.mobile_hide {
    				min-height: 0px;
    				max-height: 0px;
    				max-width: 0px;
    				display: none;
    				overflow: hidden;
    				font-size: 0px;
    			}

    			.desktop_hide {
    				display: block !important;
    				max-height: none !important;
    			}
    		}
    	</style>
    </head>

    <body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #F5F5F5;">
    	<!--[if IE]><div class="ie-browser"><![endif]-->
    	<table class="nl-container" style="table-layout: fixed; vertical-align: top; min-width: 320px; Margin: 0 auto; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #F5F5F5; width: 100%;" cellpadding="0" cellspacing="0" role="presentation" width="100%" bgcolor="#F5F5F5" valign="top">
    		<tbody>
    			<tr style="vertical-align: top;" valign="top">
    				<td style="word-break: break-word; vertical-align: top;" valign="top">
    					<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#F5F5F5"><![endif]-->
    					<div style="background-color:transparent;">
    						<div class="block-grid " style="Margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;">
    							<div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
    								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
    								<!--[if (mso)|(IE)]><td align="center" width="650" style="background-color:transparent;width:650px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
    								<div class="col num12" style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
    									<div style="width:100% !important;">
    										<!--[if (!mso)&(!IE)]><!-->
    										<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
    											<!--<![endif]-->
    											<table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
    												<tbody>
    													<tr style="vertical-align: top;" valign="top">
    														<td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
    															<table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 10px; width: 100%;" align="center" role="presentation" height="10" valign="top">
    																<tbody>
    																	<tr style="vertical-align: top;" valign="top">
    																		<td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" height="10" valign="top"><span></span></td>
    																	</tr>
    																</tbody>
    															</table>
    														</td>
    													</tr>
    												</tbody>
    											</table>
    											<!--[if (!mso)&(!IE)]><!-->
    										</div>
    										<!--<![endif]-->
    									</div>
    								</div>
    								<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    								<!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
    							</div>
    						</div>
    					</div>
    					<div style="background-color:transparent;">
    						<div class="block-grid mixed-two-up" style="Margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #FFFFFF;">
    							<div style="border-collapse: collapse;display: table;width: 100%;background-color:#FFFFFF;">
    								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px"><tr class="layout-full-width" style="background-color:#FFFFFF"><![endif]-->
    								<!--[if (mso)|(IE)]><td align="center" width="162" style="background-color:#FFFFFF;width:162px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 15px; padding-top:20px; padding-bottom:15px;"><![endif]-->
    								<div class="col num3" style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 162px; width: 162px;">
    									<div style="width:100% !important;">
    										<!--[if (!mso)&(!IE)]><!-->
    										<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:20px; padding-bottom:15px; padding-right: 0px; padding-left: 15px;">
    											<!--<![endif]-->
    											<div class="img-container center fixedwidth" align="center" style="padding-right: 25px;padding-left: 55px;">
    												<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 25px;padding-left: 55px;" align="center"><![endif]--><a href="https://www.sirmvit.edu/" target="_blank" tabindex="-1"> <img class="center fixedwidth" align="center" border="0" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/443716_423696/SIR%20MVIT%20COLLEGE%20LOGO%20%282%29.png" alt="Logo" title="Logo" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; width: 100%; max-width: 73px; display: block;" width="73"></a>
    												<!--[if mso]></td></tr></table><![endif]-->
    											</div>
    											<!--[if (!mso)&(!IE)]><!-->
    										</div>
    										<!--<![endif]-->
    									</div>
    								</div>
    								<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    								<!--[if (mso)|(IE)]></td><td align="center" width="487" style="background-color:#FFFFFF;width:487px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
    								<div class="col num9" style="display: table-cell; vertical-align: top; min-width: 320px; max-width: 486px; width: 487px;">
    									<div style="width:100% !important;">
    										<!--[if (!mso)&(!IE)]><!-->
    										<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
    											<!--<![endif]-->
    											<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 0px; padding-top: 20px; padding-bottom: 10px; font-family: 'Trebuchet MS', Tahoma, sans-serif"><![endif]-->
    											<div style="color:#555555;font-family:'Oxygen', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;line-height:1.2;padding-top:20px;padding-right:5px;padding-bottom:10px;padding-left:0px;">
    												<div style="font-family: 'Oxygen', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; font-size: 12px; line-height: 1.2; color: #555555; mso-line-height-alt: 14px;">
    													<p style="font-size: 34px; line-height: 1.2; mso-line-height-alt: 41px; margin: 0;"><span style="font-size: 34px;">Kalanjali 2019 Registration</span></p>
    												</div>
    											</div>
    											<!--[if mso]></td></tr></table><![endif]-->
    											<!--[if (!mso)&(!IE)]><!-->
    										</div>
    										<!--<![endif]-->
    									</div>
    								</div>
    								<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    								<!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
    							</div>
    						</div>
    					</div>
    					<div style="background-color:transparent;">
    						<div class="block-grid " style="Margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #C1E2F4;">
    							<div style="border-collapse: collapse;display: table;width: 100%;background-color:#C1E2F4;">
    								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px"><tr class="layout-full-width" style="background-color:#C1E2F4"><![endif]-->
    								<!--[if (mso)|(IE)]><td align="center" width="650" style="background-color:#C1E2F4;width:650px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 25px; padding-left: 25px; padding-top:5px; padding-bottom:0px;"><![endif]-->
    								<div class="col num12" style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
    									<div style="width:100% !important;">
    										<!--[if (!mso)&(!IE)]><!-->
    										<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:0px; padding-right: 25px; padding-left: 25px;">
    											<!--<![endif]-->
    											<div class="img-container center fixedwidth" align="center" style="padding-right: 0px;padding-left: 0px;">
    												<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]-->
    												<div style="font-size:1px;line-height:35px">&nbsp;</div><img class="center fixedwidth" align="center" border="0" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/443716_423696/ROYAcVhHo%20%281%29.png" alt="Image" title="Image" style="text-decoration: none; -ms-interpolation-mode: bicubic; border: 0; height: auto; width: 100%; max-width: 330px; display: block;" width="330">
    												<!--[if mso]></td></tr></table><![endif]-->
    											</div>
    											<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 15px; padding-top: 20px; padding-bottom: 0px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
    											<div style="color:#052d3d;font-family:'Lato', Tahoma, Verdana, Segoe, sans-serif;line-height:1.5;padding-top:20px;padding-right:10px;padding-bottom:0px;padding-left:15px;">
    												<div style="line-height: 1.5; font-family: 'Lato', Tahoma, Verdana, Segoe, sans-serif; font-size: 12px; color: #052d3d; mso-line-height-alt: 18px;">
    													<p style="font-size: 38px; line-height: 1.5; text-align: center; mso-line-height-alt: 57px; margin: 0;"><span style="font-size: 38px;"><strong>Registration Successful!</strong></span></p>
    													<p style="line-height: 1.5; text-align: center; font-size: 24px; mso-line-height-alt: 36px; margin: 0;"><span style="font-size: 24px;"><span style="color: #2190e3; font-size: 24px;"><span style="font-size: 24px;"><strong>Welcome,&nbsp;</strong></span></span><span style="color: #ff0000; font-size: 24px;"><span style="font-size: 24px;"><strong>{name}</strong></span></span></span></p>
    												</div>
    											</div>
    											<!--[if mso]></td></tr></table><![endif]-->
    											<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 20px; padding-left: 20px; padding-top: 20px; padding-bottom: 20px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
    											<div style="color:#555555;font-family:'Lato', Tahoma, Verdana, Segoe, sans-serif;line-height:1.2;padding-top:20px;padding-right:20px;padding-bottom:20px;padding-left:20px;">
    												<div style="font-size: 12px; line-height: 1.2; font-family: 'Lato', Tahoma, Verdana, Segoe, sans-serif; color: #555555; mso-line-height-alt: 14px;">
    													<p style="font-size: 22px; line-height: 1.2; text-align: center; mso-line-height-alt: 26px; margin: 0;"><span style="font-size: 22px; color: #000000;">Thanks for registering with us for Kalanjali 2019 events. With this email we have attached all the necessary information required for you. Kindly go through them and feel free to contact us any time.</span></p>
    												</div>
    											</div>
    											<!--[if mso]></td></tr></table><![endif]-->
    											<div class="img-container center fixedwidth" align="center" style="padding-right: 0px;padding-left: 0px;">
    												<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]-->
    												<div style="font-size:1px;line-height:45px">&nbsp;</div><img class="center fixedwidth" align="center" border="0" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/326/illo_welcome_1.png" alt="Image" title="Image" style="text-decoration: none; -ms-interpolation-mode: bicubic; border: 0; height: auto; width: 100%; max-width: 300px; display: block;" width="300">
    												<!--[if mso]></td></tr></table><![endif]-->
    											</div>
    											<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 20px; padding-left: 20px; padding-top: 20px; padding-bottom: 20px; font-family: 'Trebuchet MS', Tahoma, sans-serif"><![endif]-->
    											<div style="color:#E11212;font-family:'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;line-height:1.2;padding-top:20px;padding-right:20px;padding-bottom:20px;padding-left:20px;">
    												<div style="font-size: 12px; line-height: 1.2; font-family: 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; color: #E11212; mso-line-height-alt: 14px;">
    													<p style="font-size: 14px; line-height: 1.2; text-align: center; mso-line-height-alt: 17px; margin: 0;"><strong><span style="font-size: 20px; color: #ff0000;">Folowing are the details you have registered with us and has been successfully verified by our team.</span></strong></p>
    												</div>
    											</div>
    											<!--[if mso]></td></tr></table><![endif]-->
    											<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 50px; padding-left: 60px; padding-top: 0px; padding-bottom: 20px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
    											<div style="color:#555555;font-family:'Lato', Tahoma, Verdana, Segoe, sans-serif;line-height:1.2;padding-top:0px;padding-right:50px;padding-bottom:20px;padding-left:60px;">
    												<div style="line-height: 1.2; font-family: 'Lato', Tahoma, Verdana, Segoe, sans-serif; font-size: 12px; color: #555555; mso-line-height-alt: 14px;">
    													<p style="font-size: 18px; line-height: 1.2; text-align: center; mso-line-height-alt: 22px; margin: 0;"><span style="font-size: 18px; color: #003366;">Name : {name}</span></p>
    													<p style="font-size: 18px; line-height: 1.2; text-align: center; mso-line-height-alt: 22px; margin: 0;"><span style="font-size: 18px; color: #003366;">Email : {email}</span></p>
    													<p style="font-size: 18px; line-height: 1.2; text-align: center; mso-line-height-alt: 22px; margin: 0;"><span style="font-size: 18px; color: #003366;">Phone : {phone}</span></p>
                              <p style="font-size: 12px; line-height: 1.2; text-align: center; mso-line-height-alt: 14px; margin: 0;"><span style="font-size: 12px; color: #003366;"><span style="font-size: 12px;"><span style="font-size: 18px;">Event : {event}</span></span></span></p>
    													<p style="font-size: 12px; line-height: 1.2; text-align: center; mso-line-height-alt: 14px; margin: 0;"><span style="font-size: 12px; color: #003366;"><span style="font-size: 12px;"><span style="font-size: 18px;">College : {college}{event}</span></span></span></p>
    													<p style="font-size: 12px; line-height: 1.2; text-align: center; mso-line-height-alt: 14px; margin: 0;"><span style="font-size: 12px; color: #003366;"><span style="font-size: 12px;"><span style="font-size: 18px;">Year : {year}</span></span></span></p>
    													<p style="font-size: 12px; line-height: 1.2; text-align: center; mso-line-height-alt: 14px; margin: 0;"><span style="font-size: 12px; color: #003366;"><span style="font-size: 12px;"><span style="font-size: 18px;">Paid : INR {amount}</span></span></span></p>
    													<p style="font-size: 12px; line-height: 1.2; text-align: center; mso-line-height-alt: 14px; margin: 0;"><span style="font-size: 12px; color: #003366;"><span style="font-size: 12px;"><span style="font-size: 18px;">Transaction ID : {txn_id}</span></span></span></p>
    												</div>
    											</div>
    											<!--[if mso]></td></tr></table><![endif]-->
    											<div class="button-container" align="center" style="padding-top:20px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
    												<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-top: 20px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://bit.ly/2o8F53X" style="height:31.5pt; width:96pt; v-text-anchor:middle;" arcsize="65%" stroke="false" fillcolor="#1C4A5B"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:Tahoma, Verdana, sans-serif; font-size:16px"><![endif]--><a href="http://bit.ly/2o8F53X" target="_blank" style="-webkit-text-size-adjust: none; text-decoration: none; display: inline-block; color: #ffffff; background-color: #1C4A5B; border-radius: 27px; -webkit-border-radius: 27px; -moz-border-radius: 27px; width: auto; width: auto; border-top: 1px solid #1C4A5B; border-right: 1px solid #1C4A5B; border-bottom: 1px solid #1C4A5B; border-left: 1px solid #1C4A5B; padding-top: 5px; padding-bottom: 5px; font-family: 'Lato', Tahoma, Verdana, Segoe, sans-serif; text-align: center; mso-border-alt: none; word-break: keep-all;"><span style="padding-left:30px;padding-right:30px;font-size:16px;display:inline-block;">
    														<span style="font-size: 16px; line-height: 2; mso-line-height-alt: 32px;"><strong>VISIT US</strong></span>
    													</span></a>
    												<!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->
    											</div>
    											<table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
    												<tbody>
    													<tr style="vertical-align: top;" valign="top">
    														<td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
    															<table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #BBBBBB; width: 100%;" align="center" role="presentation" valign="top">
    																<tbody>
    																	<tr style="vertical-align: top;" valign="top">
    																		<td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
    																	</tr>
    																</tbody>
    															</table>
    														</td>
    													</tr>
    												</tbody>
    											</table>
    											<!--[if (!mso)&(!IE)]><!-->
    										</div>
    										<!--<![endif]-->
    									</div>
    								</div>
    								<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    								<!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
    							</div>
    						</div>
    					</div>
    					<div style="background-color:transparent;">
    						<div class="block-grid " style="Margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #C1E2F4;">
    							<div style="border-collapse: collapse;display: table;width: 100%;background-color:#C1E2F4;">
    								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px"><tr class="layout-full-width" style="background-color:#C1E2F4"><![endif]-->
    								<!--[if (mso)|(IE)]><td align="center" width="650" style="background-color:#C1E2F4;width:650px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:0px; padding-bottom:10px;"><![endif]-->
    								<div class="col num12" style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
    									<div style="width:100% !important;">
    										<!--[if (!mso)&(!IE)]><!-->
    										<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:0px; padding-bottom:10px; padding-right: 0px; padding-left: 0px;">
    											<!--<![endif]-->
    											<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 0px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
    											<div style="color:#555555;font-family:'Lato', Tahoma, Verdana, Segoe, sans-serif;line-height:1.5;padding-top:10px;padding-right:10px;padding-bottom:0px;padding-left:10px;">
    												<div style="font-size: 12px; line-height: 1.5; font-family: 'Lato', Tahoma, Verdana, Segoe, sans-serif; color: #555555; mso-line-height-alt: 18px;">
    													<p style="font-size: 20px; line-height: 1.5; text-align: center; mso-line-height-alt: 30px; margin: 0;"><span style="color: #000000; font-size: 20px;">With Regards, Team Kalanjali</span></p>
    													<p style="font-size: 17px; line-height: 1.5; text-align: center; mso-line-height-alt: 26px; mso-ansi-font-size: 18px; margin: 0;"><span style="font-size: 17px; color: #000080; mso-ansi-font-size: 18px;">Sir M. Visvesvaraya Institute of Technology, Bangalore</span></p>
    												</div>
    											</div>
    											<!--[if mso]></td></tr></table><![endif]-->
    											<table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
    												<tbody>
    													<tr style="vertical-align: top;" valign="top">
    														<td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;" valign="top">
    															<table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="35%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #BBBBBB; height: 0px; width: 35%;" align="center" role="presentation" height="0" valign="top">
    																<tbody>
    																	<tr style="vertical-align: top;" valign="top">
    																		<td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" height="0" valign="top"><span></span></td>
    																	</tr>
    																</tbody>
    															</table>
    														</td>
    													</tr>
    												</tbody>
    											</table>
    											<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 0px; padding-bottom: 0px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
    											<div style="color:#555555;font-family:'Lato', Tahoma, Verdana, Segoe, sans-serif;line-height:1.5;padding-top:0px;padding-right:10px;padding-bottom:0px;padding-left:10px;">
    												<div style="line-height: 1.5; font-family: 'Lato', Tahoma, Verdana, Segoe, sans-serif; font-size: 12px; color: #555555; mso-line-height-alt: 18px;">
    													<p style="line-height: 1.5; text-align: center; font-size: 14px; mso-line-height-alt: 21px; margin: 0;"><span style="font-size: 14px; color: #ffffff;"><span style="color: #000000; font-size: 14px;"><span style="font-size: 14px;">Managed by : <a style="text-decoration: underline; color: #0068A5;" href="http://bit.ly/2ppK2FR" target="_blank" rel="noopener">Techhub</a> |<a style="text-decoration: underline; color: #0068A5;" href="http://bit.ly/2nZS5ZP" target="_blank" rel="noopener"> Podnet</a></span></span></span></p>
    												</div>
    											</div>
    											<!--[if mso]></td></tr></table><![endif]-->
    											<!--[if (!mso)&(!IE)]><!-->
    										</div>
    										<!--<![endif]-->
    									</div>
    								</div>
    								<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    								<!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
    							</div>
    						</div>
    					</div>
    					<div style="background-color:transparent;">
    						<div class="block-grid " style="Margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #FFFFFF;">
    							<div style="border-collapse: collapse;display: table;width: 100%;background-color:#FFFFFF;">
    								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px"><tr class="layout-full-width" style="background-color:#FFFFFF"><![endif]-->
    								<!--[if (mso)|(IE)]><td align="center" width="650" style="background-color:#FFFFFF;width:650px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
    								<div class="col num12" style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
    									<div style="width:100% !important;">
    										<!--[if (!mso)&(!IE)]><!-->
    										<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
    											<!--<![endif]-->
    											<table class="social_icons" cellpadding="0" cellspacing="0" width="100%" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" valign="top">
    												<tbody>
    													<tr style="vertical-align: top;" valign="top">
    														<td style="word-break: break-word; vertical-align: top; padding-top: 5px; padding-right: 30px; padding-bottom: 0px; padding-left: 25px;" valign="top">
    															<table class="social_table" align="center" to="to" activate="activate" alignment="alignment" cellpadding="0" cellspacing="0" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: undefined; mso-table-tspace: 0; mso-table-rspace: 0; mso-table-bspace: 0; mso-table-lspace: 0;" valign="top">
    																<tbody>
    																	<tr style="vertical-align: top; display: inline-block; text-align: center;" align="center" valign="top">
    																		<td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 5px; padding-left: 5px;" valign="top"><a href="http://bit.ly/2nRBNSx" target="_blank"><img width="32" height="32" src="https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/facebook@2x.png" alt="Facebook" title="Facebook" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;"></a></td>
    																		<td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 5px; padding-left: 5px;" valign="top"><a href="https://twitter.com/sirmvitinfo" target="_blank"><img width="32" height="32" src="https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/twitter@2x.png" alt="Twitter" title="Twitter" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;"></a></td>
    																		<td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 5px; padding-left: 5px;" valign="top"><a href="http://bit.ly/2n07zMP" target="_blank"><img width="32" height="32" src="https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/instagram@2x.png" alt="Instagram" title="Instagram" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;"></a></td>
    																		<td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 5px; padding-left: 5px;" valign="top"><a href="http://bit.ly/2nTNPuv" target="_blank"><img width="32" height="32" src="https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/telegram@2x.png" alt="Whatsapp" title="Whatsapp" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;"></a></td>
    																	</tr>
    																</tbody>
    															</table>
    														</td>
    													</tr>
    												</tbody>
    											</table>
    											<table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
    												<tbody>
    													<tr style="vertical-align: top;" valign="top">
    														<td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;" valign="top">
    															<table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="60%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px dotted #C4C4C4; height: 0px; width: 60%;" align="center" role="presentation" height="0" valign="top">
    																<tbody>
    																	<tr style="vertical-align: top;" valign="top">
    																		<td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" height="0" valign="top"><span></span></td>
    																	</tr>
    																</tbody>
    															</table>
    														</td>
    													</tr>
    												</tbody>
    											</table>
    											<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
    											<div style="color:#4F4F4F;font-family:'Lato', Tahoma, Verdana, Segoe, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
    												<div style="font-size: 12px; line-height: 1.2; font-family: 'Lato', Tahoma, Verdana, Segoe, sans-serif; color: #4F4F4F; mso-line-height-alt: 14px;">
    													<p style="font-size: 16px; line-height: 1.2; text-align: center; mso-line-height-alt: 19px; margin: 0;"><span style="font-size: 16px;"><a style="text-decoration: underline; color: #2190E3;" href="http://bit.ly/2oEfRdt" target="_blank" rel="noopener">Transactions</a> | <a style="text-decoration: underline; color: #2190E3;" href="http://bit.ly/2oJUpE6" target="_blank" rel="noopener">Brochure</a>&nbsp;|&nbsp; <a style="text-decoration: underline; color: #2190E3;" href=" http://bit.ly/2myK0uh" target="_blank" rel="noopener">Rules & Regulations</a><span style="background-color: transparent; font-size: 16px;">&nbsp;| <a style="text-decoration: underline; color: #2190E3;" href="http://bit.ly/2o4Ovx9" target="_blank" rel="noopener">Schedule</a> | <a style="text-decoration: underline; color: #2190E3;" href="http://bit.ly/2IkjdID" target="_blank" rel="noopener">Event Location</a> | <a style="text-decoration: underline; color: #2190E3;" href="http://bit.ly/2nTNPuv" target="_blank" rel="noopener">Others</a></span></span></p>
    												</div>
    											</div>
    											<!--[if mso]></td></tr></table><![endif]-->
    											<!--[if (!mso)&(!IE)]><!-->
    										</div>
    										<!--<![endif]-->
    									</div>
    								</div>
    								<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    								<!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
    							</div>
    						</div>
    					</div>
    					<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    				</td>
    			</tr>
    		</tbody>
    	</table>
    	<!--[if (IE)]></div><![endif]-->
    </body>

    </html>

    '''.format(event=event,name=name,email=email,phone=phone,college=college,year=year,txn_id=txn_id,amount=amount)
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
                return HttpResponse(json.dumps({"message":"Registration Successful. Kindly wait for an email from us after we confirm your payment.",}),content_type="application/json")
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
