from django import forms
from django.forms import ModelForm

from .models import *


class AppointmentForm(ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'
        labels = {
            'full_name': 'Full Name',
            'email_address': 'Email',
            'phone_number': 'Phone',
            'schedule': 'Select a Schedule',
            'date': 'Date of Appointment',
            'appointment_message': 'Short Message'
        }