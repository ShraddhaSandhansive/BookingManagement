# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from AppointmentBookingSystem.models import *
from django.core.mail import send_mail
from django.conf import settings
import datetime
# Create your views here.

def test(request):
    return render(request, "Login.jinja")


def SignUp(request):
    return render(request, "SignUp.jinja")


def checkBlank(*args):
    for value in args:
        if value == "":
            return False
    return True


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
        check_blank = checkBlank(firstname, lastname, email, password, contact, address)
        if check_blank == False:
            return JsonResponse({'code' : 402})
        email_check_query = Users.objects.filter(email=email)
        if email_check_query.exists():
            return JsonResponse({'code' : 400})
        user_obj = Users()
        user_obj.name = user_name
        user_obj.email = email
        user_obj.contact = contact
        user_obj.address = address
        user_obj.isAdmin = 0
        user_obj.password = password
        user_obj.save()
        subject = user_name + ', Thank you for registering to our site '
        message = 'Your username is - ' + email + ' and your password is - ' + password + ' .'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail( subject, message, email_from, recipient_list )
        return JsonResponse({'code' : 200})
    except:
        import traceback
        print traceback.print_exc()
        return JsonResponse({'code': 500})


@csrf_exempt
def login_user(request):
    try:
        password = str(request.POST.get('password')).strip()
        username = str(request.POST.get('username')).strip()
        user_obj = Users.objects.get(email=username, password=password)
        request.session['userId'] = user_obj.user_id
        request.session['isAdmin'] = user_obj.isAdmin
        if user_obj:
            return JsonResponse({'code' : 200, 'isAdmin' : str(request.session.get('isAdmin'))})
        else:
            return JsonResponse({'code' : 500})
    except: 
        import traceback
        print traceback.print_exc()
        return JsonResponse({'code': 500})


def render_services(request):
    if request.session.get('userId') == "" or request.session.get('isAdmin') == "":
            return HttpResponse("Please login to view this page!")
    if request.session.get('isAdmin') == 1:
        return render(request, "AdminServices.jinja")
    else:
        return HttpResponse("You don't have access to view this page")


@csrf_exempt
def storeService(request):
    try:
        if request.session.get('userId') == "" or request.session.get('isAdmin') == "":
            return HttpResponse("Please login to view this page!")
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
        if request.session.get('userId') == "" or request.session.get('isAdmin') == "":
            return HttpResponse("Please login to view this page!")
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
        if request.session.get('userId') == "" or request.session.get('isAdmin') == "":
            return HttpResponse("Please login to view this page!")
        service_id = serviceId
        service_obj = Services.objects.get(service_id=service_id)
        return render(request, "bookServices.jinja", {"service": service_obj})
    except:
        import traceback
        print traceback.print_exc()
        return JsonResponse({'code': 500})


@csrf_exempt
def bookServices(request):
    try:
        if request.session.get('userId') == "" or request.session.get('isAdmin') == "":
            return HttpResponse("Please login to view this page!")
        service_id = request.POST.get('serviceId')
        booking_date = request.POST.get('bookingDate')
        formatted_date = datetime.datetime.strptime(booking_date,"%d/%m/%Y %H:%M")
        booking_obj = Bookings()
        booking_obj.serviceId_id = service_id
        booking_obj.userId_id = request.session.get('userId')
        booking_obj.booking_date = booking_date
        booking_obj.booking_status = 0
        booking_obj.save()
        user_obj = Users.objects.get(user_id=request.session.get('userId'))
        service_obj = Services.objects.get(service_id=service_id)
        subject = user_obj.name + ', Thank you for choosing our service! '
        message = 'You have requested for ' + service_obj.service_name +' on ' + booking_obj.booking_date + ' . And your total billing amount is - Rs. ' + service_obj.service_price
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user_obj.email,]
        send_mail( subject, message, email_from, recipient_list )
        return JsonResponse({'code': 200})
    except:
        import traceback
        print traceback.print_exc()
        return JsonResponse({'code': 500})


def logout_from_system(request):
    request.session['userId'] = ""
    request.session['isAdmin'] = ""
    return redirect('/login/')


def about_us(request):
    return render(request, "AboutUs.jinja")