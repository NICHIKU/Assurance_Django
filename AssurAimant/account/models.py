from django.contrib.auth.models import AbstractUser
from django.db import models

# first_name and last_name included in AbstractUser
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    bmi = models.FloatField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    smoker = models.BooleanField(default=False)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    region = models.CharField(max_length=15, blank=True, default="")
    children = models.IntegerField(null=True, blank=True)

    def compute_bmi(self):
        return round(self.weight / (self.height / 100) ** 2, 2)

    def __str__(self):
        return self.email