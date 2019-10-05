# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-10-05 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppointmentBookingSystem', '0004_auto_20191005_0530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_status', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'Bookings',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=120)),
                ('service_price', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=120)),
                ('staff_email', models.CharField(max_length=100)),
                ('staff_password', models.CharField(max_length=100)),
                ('staff_contact', models.CharField(max_length=120)),
                ('staff_address', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'Staff',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=400)),
                ('isAdmin', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.AddField(
            model_name='bookings',
            name='serviceId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppointmentBookingSystem.Services'),
        ),
        migrations.AddField(
            model_name='bookings',
            name='staffId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppointmentBookingSystem.Staff'),
        ),
        migrations.AddField(
            model_name='bookings',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppointmentBookingSystem.Users'),
        ),
    ]