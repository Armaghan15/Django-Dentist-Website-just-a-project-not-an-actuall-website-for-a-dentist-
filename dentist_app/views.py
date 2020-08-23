from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
import smtplib

from .models import Appointment
from .forms import AppointmentForm


from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.



# ----------------------(first View)------------------------
# The Home view for the home page
def Home(request):
	return render(request, 'dentist_app/home.html')


# ----------------------(Second View)------------------------
# The About view for the about page
def About(request):
	return render(request, 'dentist_app/about.html')



# ----------------------(Third View)------------------------
# The Contact view for the contact page
def Contact(request):
	if request.method == 'POST':
		contact_fullname = request.POST.get('contact_fullname')
		contact_email = request.POST.get('contact_email')
		message = request.POST.get('message')

		html_message = render_to_string(
        	'dentist_app/email.html',
        	{'contact_fullname': contact_fullname,'contact_email': contact_email, 'message': message}
		)

		plain_message = strip_tags(html_message)
		html_message = html_message.replace("\r\n", "<br>")

		send_mail(
		"From: " + contact_fullname, # Subject
		plain_message,  # Message
		contact_email, # From Email
		['a.orakzai2020@gmail.com', contact_email],  # To Email
		)

		context = {
			'contact_fullname': contact_fullname,
			'contact_email': contact_email,
			'message': message,
  		}

		return render(request, 'dentist_app/contact.html', context)

	else:
		return render(request, 'dentist_app/contact.html')


# ----------------------(Fourth View)----------------------
# Function for booking an appointment
def CreateAppointment(request):

	appointment = Appointment.objects.all()
	appointment_form = AppointmentForm()

	if request.method == 'POST':
		appointment_form = AppointmentForm(request.POST)

		if appointment_form.is_valid():
			appointment_form.save()


		full_name = appointment_form.cleaned_data['full_name']
		email_address = appointment_form.cleaned_data['email_address']
		phone_number = appointment_form.cleaned_data['phone_number']
		schedule = appointment_form.cleaned_data['schedule']
		date = appointment_form.cleaned_data['date']
		appointment_message =appointment_form.cleaned_data['appointment_message']


		html_message = render_to_string(
        	'dentist_app/appointment_email.html',
        	{'full_name': full_name,'email_address': email_address, 'appointment_message': appointment_message, 'schedule': schedule, 'date': date, 'phone_number': phone_number}
		) 

		plain_message = strip_tags(html_message)
		html_message = html_message.replace("\r\n", "<br>")

		send_mail(
		"From: " + full_name, # Subject
		plain_message,  # Message
		email_address, # From Email
		['a.orakzai2020@gmail.com'],  # To Email
		)

		context = {
			'appointment_form': appointment_form, 
			'appointment': appointment, 
			'full_name': full_name, 
			'email_address': email_address, 
			'phone_number': phone_number, 
			'schedule': schedule, 
			'date': date
			} 

		return render(request, 'dentist_app/appointment_msg.html', context)

	else:
		context = {'appointment_form': appointment_form, 'appointment': appointment} 
		return render(request, 'dentist_app/appointment.html', context)




# ----------------------(Fifth View)------------------------
# The Services view for the services page
def ServicesAndPricing(request):
	return render(request, 'dentist_app/servicesandpricing.html')



# ----------------------(Sixth View)------------------------
# The Testimonials view for the Testimonials page
def Testimonials(request):
	return render(request, 'dentist_app/testimonials.html')
