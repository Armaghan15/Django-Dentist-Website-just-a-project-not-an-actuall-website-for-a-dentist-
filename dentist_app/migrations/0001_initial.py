# Generated by Django 3.0.8 on 2020-08-20 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=200)),
                ('phone_number', models.IntegerField(unique=True)),
                ('schedule', models.CharField(choices=[('9AM to 12PM', '9AM to 12PM'), ('1PM to 3PM', '1PM to 3PM'), ('4PM to 7PM', '4PM to 7PM')], default='9AM to 12PM', max_length=11)),
                ('date', models.DateField(default=datetime.date.today)),
                ('form_message', models.CharField(max_length=300)),
            ],
        ),
    ]
