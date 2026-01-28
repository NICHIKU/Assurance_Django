from django.urls import path
<<<<<<< HEAD
from .views import UserProfileView, AccountModificationView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/modif/', AccountModificationView.as_view(), name='profile_modif'),
]
=======
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register")
]
>>>>>>> f83379f781fe660dab62e3d594c1f81d77f27ab1
