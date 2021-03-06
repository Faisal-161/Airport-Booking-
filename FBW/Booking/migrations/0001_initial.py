# Generated by Django 4.0.5 on 2022-07-06 17:11

import Booking.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.CharField(default=Booking.models.random_string, editable=False, max_length=6, unique=True)),
                ('passenger_first_name', models.CharField(max_length=20)),
                ('passenger_last_name', models.CharField(max_length=20)),
                ('booking_datetime', models.DateTimeField(auto_now_add=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Flight.flight')),
            ],
        ),
    ]
