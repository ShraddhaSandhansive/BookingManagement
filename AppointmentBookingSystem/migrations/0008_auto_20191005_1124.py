# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-10-05 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppointmentBookingSystem', '0007_services_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_image',
            field=models.CharField(default=b'', max_length=500000),
        ),
    ]
