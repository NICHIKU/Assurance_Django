from django.urls import path
from .views import MakePredictionView

urlpatterns = [
    path('predict', MakePredictionView.as_view(), name='predict'),
]