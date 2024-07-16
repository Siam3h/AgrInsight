from rest_framework import serializers
from .models import CropYieldInput

class CropYieldInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropYieldInput
        fields = ['year', 'area', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp']
