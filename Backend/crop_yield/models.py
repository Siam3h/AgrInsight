from django.db import models

class CropYieldInput(models.Model):
    year = models.IntegerField()
    area = models.CharField(max_length=255)
    average_rain_fall_mm_per_year = models.FloatField()
    pesticides_tonnes = models.FloatField()
    avg_temp = models.FloatField()
