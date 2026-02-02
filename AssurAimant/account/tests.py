from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.
class CustomUserTest(TestCase):
    def test_email_uniqueness(self):
            """Test unicité de l'email"""
            User.objects.create_user(
                username='user1@example.com',
                email='user1@example.com',
                password='pass123'
            )
            with self.assertRaises(Exception):
                User.objects.create_user(
                    username='user2@example.com',
                    email='user1@example.com',  # Même email
                    password='pass456'
                )
class CustomUserFormTest(TestCase):
    def test_valid_registration_form(self):
        """Test formulaire d'inscription valide"""
        from account.forms import CustomUserForm
        form_data = {
            'first_name': 'Marie',
            'last_name': 'Martin',
            'email': 'marie.martin@test.com',
            'password': 'Password123'
        }
        form = CustomUserForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_invalid_email_in_form(self):
        """Test formulaire avec email invalide"""
        from account.forms import CustomUserForm
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalid-email',
            'password': 'Password123'
        }
        form = CustomUserForm(data=form_data)
        self.assertFalse(form.is_valid())
    def test_duplicate_email_in_form(self):
        """Test formulaire avec email déjà existant"""
        User.objects.create_user(
            username='existing@test.com',
            email='existing@test.com',
            password='pass123'
        )
        from account.forms import CustomUserForm
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'existing@test.com',  # Email déjà utilisé
            'password': 'Password123'
        }
        form = CustomUserForm(data=form_data)
        self.assertFalse(form.is_valid())
    def test_password_too_short(self):
        """Test mot de passe trop court"""
        from account.forms import CustomUserForm
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@test.com',
            'password': 'short'  # Moins de 8 caractères
        }
        form = CustomUserForm(data=form_data)
        self.assertFalse(form.is_valid())
    def test_password_no_uppercase(self):
        """Test mot de passe sans majuscule"""
        from account.forms import CustomUserForm
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@test.com',
            'password': 'nouveau123'  # Pas de majuscule
        }
        form = CustomUserForm(data=form_data)
        self.assertFalse(form.is_valid())
    def test_password_no_digit(self):
        """Test mot de passe sans chiffre"""
        from account.forms import CustomUserForm
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@test.com',
            'password': 'Nouveau'  # Pas de chiffre
        }
        form = CustomUserForm(data=form_data)
        self.assertFalse(form.is_valid())