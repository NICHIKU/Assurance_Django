from django.urls import path
from .views import AccountModificationView, RegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('profile', AccountModificationView.as_view(), name='profile'),
    path('register', RegisterView.as_view(), name="register"),
    path('login', UserLoginView.as_view(), name="login"),
    path('logout', UserLogoutView.as_view(), name="logout"),
]
