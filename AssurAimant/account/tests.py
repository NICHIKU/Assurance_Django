from django.test import TestCase
from .models import CustomUser

# Create your tests here.
class CustomUserTest(TestCase):

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

    def test_bmi_calculation(self):
        user = CustomUser(height=180, weight=80)
        self.assertEqual(user.compute_bmi(), 24.69)