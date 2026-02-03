from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Advisor, Appointment
from .forms import AppointmentForm

User = get_user_model()

@login_required
def appointment_booking(request):
    if request.user.user_type == 'advisor':
        return redirect('advisor_dashboard')
    
    advisors = Advisor.objects.all()
    print(f"DEBUG: Nombre de conseillers trouvés: {advisors.count()}")
    for advisor in advisors:
        print(f"DEBUG: Conseiller: {advisor}")
    
    # Si aucun conseiller n'existe, afficher un message d'erreur
    if not advisors.exists():
        return render(request, 'appointment/no_advisor.html', {
            'message': 'Aucun conseiller n\'est disponible pour le moment. Veuillez réessayer plus tard.'
        })
    
    selected_advisor = None
    available_slots = []
    
    if request.method == 'POST':
        advisor_id = request.POST.get('advisor')
        selected_date = request.POST.get('date')
        selected_time = request.POST.get('time')
        
        if advisor_id:
            selected_advisor = get_object_or_404(Advisor, id=advisor_id)
            
            if selected_date:
                available_slots = get_available_slots(selected_advisor, selected_date)
                
                # Si un créneau horaire est sélectionné, créer le rendez-vous
                if selected_time:
                    appointment = Appointment.objects.create(
                        client=request.user,
                        advisor=selected_advisor,
                        date=selected_date,
                        time=selected_time,
                        status='pending'
                    )
                    return redirect('appointment_success', appointment_id=appointment.id)
    
    context = {
        'advisors': advisors,
        'selected_advisor': selected_advisor,
        'available_slots': available_slots,
        'selected_date': selected_date if 'selected_date' in locals() else None,
        'today': timezone.now().date(),
    }
    return render(request, 'appointment/booking.html', context)

def get_available_slots(advisor, date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    
    # Créer tous les créneaux possibles (9h-18h, par heure)
    all_slots = []
    for hour in range(9, 19):
        time_obj = datetime.strptime(f'{hour:02d}:00', '%H:%M').time()
        all_slots.append(time_obj)
    
    # Récupérer les créneaux déjà pris
    booked_slots = Appointment.objects.filter(
        advisor=advisor,
        date=date_obj,
        status__in=['pending', 'confirmed']
    ).values_list('time', flat=True)
    
    # Filtrer les créneaux disponibles
    available = [slot for slot in all_slots if slot not in booked_slots]
    
    # Ne pas permettre les rendez-vous dans le passé
    now = timezone.now()
    if date_obj == now.date():
        available = [slot for slot in available if slot > now.time()]
    
    return available

@login_required
def create_appointment(request):
    if request.method == 'POST':
        advisor_id = request.POST.get('advisor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        advisor = get_object_or_404(Advisor, id=advisor_id)
        
        appointment = Appointment.objects.create(
            client=request.user,
            advisor=advisor,
            date=date,
            time=time,
            status='pending'
        )
        
        return redirect('appointment_success', appointment_id=appointment.id)
    
    return redirect('appointment_booking')

@login_required
def appointment_success(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, client=request.user)
    return render(request, 'appointment/success.html', {'appointment': appointment})

@login_required
def my_appointments(request):
    if request.user.user_type == 'advisor':
        appointments = Appointment.objects.filter(advisor__user=request.user)
    else:
        appointments = Appointment.objects.filter(client=request.user)
    
    return render(request, 'appointment/my_appointments.html', {'appointments': appointments})

@login_required
def advisor_dashboard(request):
    if request.user.user_type != 'advisor':
        return redirect('appointment_booking')
    
    advisor = get_object_or_404(Advisor, user=request.user)
    today_appointments = Appointment.objects.filter(
        advisor=advisor,
        date=timezone.now().date()
    )
    upcoming_appointments = Appointment.objects.filter(
        advisor=advisor,
        date__gt=timezone.now().date(),
        status__in=['pending', 'confirmed']
    )
    
    context = {
        'advisor': advisor,
        'today_appointments': today_appointments,
        'upcoming_appointments': upcoming_appointments,
    }
    return render(request, 'appointment/advisor_dashboard.html', context)

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    # Vérifier les permissions
    if appointment.client != request.user and appointment.advisor.user != request.user:
        return redirect('appointment_booking')
    
    appointment.status = 'cancelled'
    appointment.save()
    
    return redirect('my_appointments')

@login_required
def confirm_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    # Seul le conseiller peut confirmer
    if appointment.advisor.user != request.user:
        return redirect('appointment_booking')
    
    appointment.status = 'confirmed'
    appointment.save()
    
    return redirect('advisor_dashboard')    