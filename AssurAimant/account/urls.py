from django.urls import path
from .views import UserProfileView, AccountModificationView, RegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('profile', UserProfileView.as_view(), name='profile'),
    path('profile-modif', AccountModificationView.as_view(), name='profile_modif'),
    path('register', RegisterView.as_view(), name="register"),
    path('login', UserLoginView.as_view(), name="login"),
    path('logout', UserLogoutView.as_view(), name="logout"),
]
