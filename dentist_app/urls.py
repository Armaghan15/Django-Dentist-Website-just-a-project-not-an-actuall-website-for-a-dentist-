from django.urls import path
from . import views

urlpatterns = [
	path('', views.Home, name='home'),
	path('about/', views.About, name='about'),
	path('contact/', views.Contact, name='contact'),
	path('appointment/', views.CreateAppointment, name='appointment'),
	path('services_and_pricing/', views.ServicesAndPricing, name='services_and_pricing'),
	path('testimonials/', views.Testimonials, name='testimonials')
]
