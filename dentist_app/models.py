from django.db import models

import datetime

# Create your models here.

SCHEDULE_CHOICES = (
        ('9AM to 12PM', '9AM to 12PM'),
        ('1PM to 3PM', '1PM to 3PM'),
        ('4PM to 7PM', '4PM to 7PM'),
    )



class Appointment(models.Model):
    full_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=10)
    schedule = models.CharField(max_length=11, choices=SCHEDULE_CHOICES, default='9AM to 12PM')
    date = models.DateField(default=datetime.date.today)
    appointment_message = models.CharField(max_length=250, default='I want to book an appointment')


    def __repr__ (self):
        return self.full_name