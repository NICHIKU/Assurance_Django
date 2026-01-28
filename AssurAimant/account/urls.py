from django.urls import path
from .views import UserProfileView, AccountModificationView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/modif/', AccountModificationView.as_view(), name='profile_modif'),
]
