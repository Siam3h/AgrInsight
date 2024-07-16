from django.urls import path
from .views import PredictYield, YieldGraph

urlpatterns = [
    path('yield_predict/', PredictYield.as_view(), name='predict_yield'),
    path('yield_graph/', YieldGraph.as_view(), name='yield_graph'),
]
