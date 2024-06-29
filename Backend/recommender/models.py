from django.db import models
from django.conf import settings

class ModelMetadata(models.Model):
    model_type = models.CharField(max_length=50)# Classifier or Regressor
    input_description = models.TextField(null=True, blank=True)
    date_trained = models.DateTimeField(auto_now_add=True)
    accuracy = models.CharField(max_length=10, default="N/A", blank=True)
    f1_score = models.CharField(max_length=10, default="N/A", blank=True)
    precision = models.CharField(max_length=10, default="N/A", blank=True)
    recall = models.CharField(max_length=10, default="N/A", blank=True)
    regressor_score = models.CharField(max_length=10, default="N/A", blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.model_type} trained on {self.date_trained}"
    

