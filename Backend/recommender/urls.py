from django.urls import path
from .views import train_classifier, train_regressor, evaluate, predict

urlpatterns = [
    path('train_classifier/', train_classifier, name='train_classifier'),
    path('train_regressor/', train_regressor, name='train_regressor'),
    path('evaluate/', evaluate, name='evaluate'),
    path('predict/', predict, name='predict'),
]
