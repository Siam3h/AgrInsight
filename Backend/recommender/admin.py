from django.contrib import admin
from recommender.models import ModelMetadata


@admin.register(ModelMetadata)
class ModelMetadataAdmin(admin.ModelAdmin):
    list_display = ['model_type','date_trained','accuracy',
                    'f1_score','precision',
                    'recall','regressor_score','user']
    list_filter = ['model_type']
    search_fields = ['model_type','accuracy','regressor_score','user__username']
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created
            obj.user = request.user
        super().save_model(request, obj, form, change)

