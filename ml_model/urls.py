# ml_model/urls.py

from django.urls import path
from .views import predict_view

app_name = 'ml_model'

urlpatterns = [
    path('predict-loan/', predict_view, name='predict-loan'),
]
