from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import time

User = get_user_model()

class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.speciality}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmé'),
        ('cancelled', 'Annulé'),
        ('completed', 'Terminé'),
    ]
    
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_appointments')
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE, related_name='advisor_appointments')
    date = models.DateField()
    time = models.TimeField(
        validators=[
            MinValueValidator(time(9, 0)),
            MaxValueValidator(time(18, 0))
        ]
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['advisor', 'date', 'time']
        ordering = ['date', 'time']
    
    def __str__(self):
        return f"Rendez-vous {self.date} {self.time} - {self.client.email}"