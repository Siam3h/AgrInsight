from rest_framework import serializers
from .models import ModelMetadata

class ModelMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelMetadata
        fields = '__all__'
