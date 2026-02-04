from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from unittest.mock import patch, MagicMock
from .models import CustomUser
from .forms import CustomUserForm, ModificationForm, CustomLoginForm
from .views import (
    UserProfileView,
    AccountModificationView,
    RegisterView,
    UserLoginView,
    UserLogoutView,
    home_view
)
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

    def setUp(self):
        self.basicUser = CustomUser.objects.create(
            username = "jeandupont",
            first_name = "Jean",
            last_name = "Dupont",
            email = 'toto@gmail.com',
        )

        self.completeUser = CustomUser.objects.create(
            username = "jean.dupont",
            first_name = "Jean",
            last_name = "Dupont",
            email = 'toto1@gmail.com',
            age = 25,
            smoker = False,
            height = 176,
            weight = 70,
            bmi = 22,
            region = 1,
            children = 0,
        )

    def test_user_base_info(self):
        self.assertEqual(self.basicUser.first_name, 'Jean')
        self.assertEqual(self.basicUser.last_name, 'Dupont')
        self.assertEqual(self.basicUser.email, 'toto@gmail.com')
    
    def test_user_info(self):
        self.assertIsInstance(self.completeUser, CustomUser)

        self.assertEqual(self.completeUser.email, 'toto1@gmail.com')
        self.assertEqual(self.completeUser.age, 25)
        self.assertEqual(self.completeUser.smoker, False)
        self.assertEqual(self.completeUser.height, 176)
        self.assertEqual(self.completeUser.weight, 70)
        self.assertEqual(self.completeUser.bmi, 22)
        self.assertEqual(self.completeUser.region, 1)
        self.assertEqual(self.completeUser.children, 0)

    def test_bdd_user_check(self):
        users = CustomUser.objects.all()
        self.assertEqual(len(users), 2)
        
    def test_bdd_user_deletion(self):
        self.basicUser.delete()
        users = CustomUser.objects.all()
        self.assertEqual(len(users), 1)
            

    def test_bmi_calculation(self):
        user = CustomUser(height=180, weight=80)
        self.assertEqual(user.compute_bmi(), 24.69)
        
User = get_user_model()


class BaseTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        
        self.user = User.objects.create_user(
            username='testuser@test.com',
            email='testuser@test.com',
            password='TestPassword123!',
            first_name='John',
            last_name='Doe',
            age=30,
            smoker=False,
            height=175,
            weight=70,
            sex='M',
            region='FR',
            children=2
        )
        
        self.user.is_verified = True
        self.user.save()
        
        self.unverified_user = User.objects.create_user(
            username='unverified@test.com',
            email='unverified@test.com',
            password='TestPassword123!',
            first_name='Jane',
            last_name='Smith'
        )
        self.unverified_user.is_verified = False
        self.unverified_user.save()


class AccountModificationViewTest(BaseTestCase):
    
    def test_modification_view_get_authenticated(self):
        self.client.login(username='testuser@test.com', password='TestPassword123!')
        response = self.client.get(reverse('profile'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/profile_modif.html')
        self.assertIsInstance(response.context['form'], ModificationForm)
    
    def test_modification_view_form_initial_data(self):
        self.client.login(username='testuser@test.com', password='TestPassword123!')
        response = self.client.get(reverse('profile'))
        
        form = response.context['form']
        self.assertEqual(form.initial['first_name'], 'John')
        self.assertEqual(form.initial['last_name'], 'Doe')
        self.assertEqual(form.initial['email'], 'testuser@test.com')
        self.assertEqual(form.initial['age'], 30)
        self.assertEqual(form.initial['height'], 175)
        self.assertEqual(form.initial['weight'], 70)
        self.assertEqual(form.initial['sex'], 'M')
        self.assertEqual(form.initial['region'], 'FR')
        self.assertEqual(form.initial['children'], 2)
    
    def test_modification_view_post_valid_data(self):
        self.client.login(username='testuser@test.com', password='TestPassword123!')
        
        data = {
            'first_name': 'Johnny',
            'last_name': 'Updated',
            'email': 'newemail@test.com',
            'age': 35,
            'children': 3,
            'height': 180,
            'weight': 75,
            'smoker': 'yes',
            'sex': 'male',
            'region': 'northeast'
        }
        
        response = self.client.post(reverse('profile'), data)
        self.assertEqual(response.status_code, 302)
        
        self.user.refresh_from_db()
        
        self.assertEqual(self.user.first_name, 'Johnny')
        self.assertEqual(self.user.last_name, 'Updated')
        self.assertEqual(self.user.email, 'newemail@test.com')
        self.assertEqual(self.user.age, 35)
        self.assertEqual(self.user.children, 3)
        self.assertEqual(self.user.height, 180)
        self.assertEqual(self.user.weight, 75)
        self.assertTrue(self.user.smoker)
        self.assertEqual(self.user.sex, 'male')
        self.assertEqual(self.user.region, 'northeast')
    
    def test_modification_view_post_invalid_data(self):
        self.client.login(username='testuser@test.com', password='TestPassword123!')
        
        data = {
            'first_name': '',
            'last_name': 'Updated',
            'email': 'invalid-email',
        }
        
        response = self.client.post(reverse('profile'), data)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/profile_modif.html')
        
        form = response.context['form']
        self.assertFalse(form.is_valid())
    
    def test_modification_view_smoker_conversion(self):
        self.client.login(username='testuser@test.com', password='TestPassword123!')
        
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'testuser@test.com',
            'age': 30,
            'children': 2,
            'height': 175,
            'weight': 70,
            'smoker': 'yes',
            'sex': 'male',
            'region': 'northeast'
        }
        
        self.client.post(reverse('profile'), data)
        self.user.refresh_from_db()
        self.assertTrue(self.user.smoker)
        
        data['smoker'] = 'no'
        self.client.post(reverse('profile'), data)
        self.user.refresh_from_db()
        self.assertFalse(self.user.smoker)
    
    def test_modification_view_computes_bmi(self):
        self.client.login(username='testuser@test.com', password='TestPassword123!')
        
        with patch.object(CustomUser, 'compute_bmi', return_value=22.5) as mock_bmi:
            data = {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'testuser@test.com',
                'age': 30,
                'children': 2,
                'height': 175,
                'weight': 70,
                'smoker': 'no',
                'sex': 'male',
                'region': 'northeast'
            }
            
            self.client.post(reverse('profile'), data)
            mock_bmi.assert_called_once()
    
    def test_modification_view_requires_authentication(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 401)


class RegisterViewTest(BaseTestCase):
    
    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')
        self.assertIsInstance(response.context['form'], CustomUserForm)
    
    def test_register_view_post_valid_data(self):
        data = {
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@test.com',
            'password': 'SecurePassword123!',
            'password_confirm': 'SecurePassword123!'
        }
        
        response = self.client.post(reverse('register'), data)
        self.assertRedirects(response, reverse('login'))
        
        user_exists = User.objects.filter(email='newuser@test.com').exists()
        self.assertTrue(user_exists)
        
        new_user = User.objects.get(email='newuser@test.com')
        self.assertEqual(new_user.username, 'newuser@test.com')
        self.assertNotEqual(new_user.password, 'SecurePassword123!')
        self.assertTrue(new_user.check_password('SecurePassword123!'))
    
    def test_register_view_post_invalid_data(self):
        data = {
            'first_name': '',
            'last_name': 'User',
            'email': 'invalid-email',
            'password': 'weak',
        }
        
        response = self.client.post(reverse('register'), data)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')
        
        form = response.context['form']
        self.assertFalse(form.is_valid())
        
        user_exists = User.objects.filter(email='invalid-email').exists()
        self.assertFalse(user_exists)
    
    def test_register_view_duplicate_email(self):
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@test.com',
            'password': 'SecurePassword123!',
            'password_confirm': 'SecurePassword123!'
        }
        
        response = self.client.post(reverse('register'), data)
        
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())


class UserLoginViewTest(BaseTestCase):
    
    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/login.html')
        self.assertIsInstance(response.context['form'], CustomLoginForm)
    
    def test_login_view_post_valid_credentials(self):
        data = {
            'username': 'testuser@test.com',
            'password': 'TestPassword123!'
        }
        
        response = self.client.post(reverse('login'), data)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)
    
    def test_login_view_post_invalid_credentials(self):
        data = {
            'username': 'testuser@test.com',
            'password': 'WrongPassword!'
        }
        
        response = self.client.post(reverse('login'), data)
        
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        
        form = response.context['form']
        self.assertFalse(form.is_valid())
    
    def test_login_view_redirect_authenticated_user(self):
        self.client.login(username='testuser@test.com', password='TestPassword123!')
        response = self.client.get(reverse('login'))
        self.assertRedirects(response, reverse('home'))
    
    def test_login_view_get_success_url(self):
        view = UserLoginView()
        success_url = view.get_success_url()
        self.assertEqual(success_url, reverse('home'))


class UserLogoutViewTest(BaseTestCase):
    
    def test_logout_view(self):
        self.client.login(username='testuser@test.com', password='TestPassword123!')
        
        response = self.client.get(reverse('home'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
    
    def test_logout_view_next_page(self):
        view = UserLogoutView()
        self.assertEqual(view.next_page, reverse('login'))





class EdgeCasesTest(BaseTestCase):
    
    def test_modification_with_nullable_fields_empty(self):
        minimal_user = User.objects.create_user(
            username='minimal@test.com',
            email='minimal@test.com',
            password='TestPassword123!',
            first_name='Min',
            last_name='User'
        )
        minimal_user.is_verified = True
        minimal_user.save()
        
        self.client.login(username='minimal@test.com', password='TestPassword123!')
        response = self.client.get(reverse('profile'))
        
        form = response.context['form']
        self.assertIsNone(form.initial.get('age'))
        self.assertIsNone(form.initial.get('smoker'))
        self.assertIsNone(form.initial.get('height'))
        self.assertIsNone(form.initial.get('weight'))
        self.assertIsNone(form.initial.get('sex'))
        self.assertIsNone(form.initial.get('region'))
        self.assertIsNone(form.initial.get('children'))
    
    def test_register_username_equals_email(self):
        
        data = {
            'first_name': 'Test',
            'last_name': 'Username',
            'email': 'test.username@example.com',
            'password': 'SecurePassword123!',
            'password_confirm': 'SecurePassword123!'
        }
        
        self.client.post(reverse('register'), data)
        
        user = User.objects.get(email='test.username@example.com')
        self.assertEqual(user.username, user.email)

class IntegrationTest(BaseTestCase):
    
    def test_full_registration_login_modification_flow(self):
        register_data = {
            'first_name': 'Integration',
            'last_name': 'Test',
            'email': 'integration@test.com',
            'password': 'SecurePassword123!',
            'password_confirm': 'SecurePassword123!'
        }
        
        response = self.client.post(reverse('register'), register_data)
        self.assertRedirects(response, reverse('login'))
        
        login_data = {
            'username': 'integration@test.com',
            'password': 'SecurePassword123!'
        }
        
        user = User.objects.get(email='integration@test.com')
        user.is_verified = True
        user.save()
        
        response = self.client.post(reverse('login'), login_data)
        self.assertRedirects(response, reverse('home'))
        
        modification_data = {
            'first_name': 'Updated Integration',
            'last_name': 'Test Updated',
            'email': 'integration@test.com',
            'age': 25,
            'children': 0,
            'height': 170,
            'weight': 65,
            'smoker': 'no',
            'sex': 'female',
            'region': 'southeast'
        }
        
        response = self.client.post(reverse('profile'), modification_data)
        self.assertEqual(response.status_code, 302)
        
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Updated Integration')
        self.assertEqual(user.age, 25)
        
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('login'))

User = get_user_model()


   
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
