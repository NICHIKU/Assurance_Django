from django.urls import path
from . import views

app_name = 'appointment'

urlpatterns = [
    path('booking/', views.appointment_booking, name='booking'),
    path('create/', views.create_appointment, name='create_appointment'),
    path('success/<int:appointment_id>/', views.appointment_success, name='appointment_success'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path('advisor-dashboard/', views.advisor_dashboard, name='advisor_dashboard'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('confirm/<int:appointment_id>/', views.confirm_appointment, name='confirm_appointment'),
]