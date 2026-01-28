from django.contrib import admin

from .models import User, UserInformation

# Register your models here.
admin.site.register(User)
admin.site.register(UserInformation)