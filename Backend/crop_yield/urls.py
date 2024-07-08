from django.urls import path
from .views import PredictYield

urlpatterns = [
    path('yield_predict/', PredictYield.as_view(), name='predict_yield')
]
