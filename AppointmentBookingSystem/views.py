# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from AppointmentBookingSystem.models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def test(request):
    return render(request, "Login.jinja")


def SignUp(request):
    return render(request, "SignUp.jinja")

@csrf_exempt
def storeUser(request):
    try:
        firstname = str(request.POST.get('firstname')).strip()
        lastname = str(request.POST.get('lastname')).strip()
        user_name = firstname + " " + lastname
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        user_obj = Users()
        user_obj.name = user_name
        user_obj.email = email
        user_obj.contact = contact
        user_obj.address = address
        user_obj.isAdmin = 0
        user_obj.password = password
        user_obj.save()
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['shraddhasandhansive@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        return JsonResponse({'code' : 200})
    except:
        import traceback
        print traceback.print_exc()
        test = {
        "code": str(traceback.format_exc())
        }
        return JsonResponse(test)


@csrf_exempt
def login_user(request):
    try:
        password = str(request.POST.get('password')).strip()
        username = str(request.POST.get('username')).strip()
        user_obj = Users.objects.get(email=username, password=password)
        request.session['userId'] = user_obj.user_id
        if user_obj:
            return JsonResponse({'code' : 200, 'msg' : str(request.session.get('userId'))})
        else:
            return JsonResponse({'code' : 500})
    except: 
        import traceback
        print traceback.print_exc()
        test = {
        "code": str(traceback.format_exc())
        }
        return JsonResponse(test)


def render_services(request):
    return render(request, "AdminServices.jinja")


@csrf_exempt
def storeService(request):
    try:
        service_price = request.POST.get('price')
        service_name = request.POST.get('name')
        service_image = request.POST.get('imageFile')
        service_obj = Services()
        service_obj.service_name = service_name
        service_obj.service_price = service_price
        service_obj.service_image = service_image
        service_obj.save()
        return JsonResponse({'code': 200})
    except:
        return JsonResponse({'code': 500})
        

@csrf_exempt
def render_all_services(request):
    try:
        service_list = Services.objects.all()
        services = []
        for service in service_list:
            services.append(service)
        return render(request, "ShowServices.jinja", {"services": services})
    except:
        import traceback
        print traceback.print_exc()
        return JsonResponse({'code': 500})


@csrf_exempt
def serviceSelected(request, serviceId):
    try:
        service_id = serviceId
        service_obj = Services.objects.get(service_id=service_id)
        return render(request, "bookServices.jinja", {"service": service_obj})
    except:
        import traceback
        print traceback.print_exc()
        return JsonResponse({'code': 500})
