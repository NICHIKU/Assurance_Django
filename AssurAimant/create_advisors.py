#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AssurAimant.settings')
django.setup()

from django.contrib.auth import get_user_model
from appointment.models import Advisor

User = get_user_model()

# Créer des conseillers de test
advisors_data = [
    {
        'email': 'martin.durand@assuraimant.fr',
        'first_name': 'Martin',
        'last_name': 'Durand',
        'password': 'password123',
        'speciality': 'Assurance Vie',
        'phone': '0123456789'
    },
    {
        'email': 'sophie.bernard@assuraimant.fr',
        'first_name': 'Sophie',
        'last_name': 'Bernard',
        'password': 'password123',
        'speciality': 'Assurance Auto',
        'phone': '0234567890'
    },
    {
        'email': 'pierre.martin@assuraimant.fr',
        'first_name': 'Pierre',
        'last_name': 'Martin',
        'password': 'password123',
        'speciality': 'Assurance Habitation',
        'phone': '0345678901'
    }
]

for advisor_data in advisors_data:
    # Vérifier si l'utilisateur existe déjà
    if User.objects.filter(email=advisor_data['email']).exists():
        print(f"L'utilisateur {advisor_data['email']} existe déjà")
        continue
    
    # Créer l'utilisateur conseiller
    user = User.objects.create_user(
        email=advisor_data['email'],
        first_name=advisor_data['first_name'],
        last_name=advisor_data['last_name'],
        password=advisor_data['password'],
        user_type='advisor'
    )
    
    # Créer le conseiller associé
    advisor = Advisor.objects.create(
        user=user,
        speciality=advisor_data['speciality'],
        phone=advisor_data['phone']
    )
    
    print(f"Conseiller créé: {advisor}")

print("\nCréation des conseillers terminée!")
print(f"Total conseillers: {Advisor.objects.count()}")
