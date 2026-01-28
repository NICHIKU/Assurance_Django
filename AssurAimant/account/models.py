from django.contrib.auth.models import AbstractUser
from django.db import models

# first_name and last_name included in AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # The client depends on the user
    bmi = models.FloatField()
    age = models.IntegerField()
    smoker = models.BooleanField()
    region = models.CharField(max_length=15)
    children = models.IntegerField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"