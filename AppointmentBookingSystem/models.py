# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.conf.urls import include
from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=120)
    address = models.CharField(max_length=400)
    isAdmin = models.SmallIntegerField()     # 0 - user, 1 - admin, 2 - staff

    class Meta:
        db_table = 'Users'


class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=120)
    service_price = models.CharField(max_length=120)
    service_image = models.CharField(max_length=500000, default="")

    class Meta:
        db_table = 'Services'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=120)
    staff_email = models.CharField(max_length=100)
    staff_password = models.CharField(max_length=100)
    staff_contact = models.CharField(max_length=120)
    staff_address = models.CharField(max_length=400)
    
    
    class Meta:
        db_table = 'Staff'


class Bookings(models.Model):
    booking_id = models.AutoField(primary_key=True)
    serviceId = models.ForeignKey(Services, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    # staffId = models.ForeignKey(Staff, on_delete=models.CASCADE, default = "")
    booking_status = models.SmallIntegerField()     # 0 - placed, 1 - Confirmed, 2 - Cancelled, 3 - Postponed
    booking_date = models.CharField(max_length=100)
    class Meta:
        db_table = 'Bookings'