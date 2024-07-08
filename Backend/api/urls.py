from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import  permission_classes

schema_view = get_schema_view(
    openapi.Info(
        title="Agri Insight API Documentation",
        default_version='v1',
        description=(
            "Welcome to the Agri Insight API documentation. The Agri Insight API provides access to a suite of endpoints "
            "designed to support a machine learning platform for agricultural purposes. Through this API, users, including "
            "farmers and agricultural enthusiasts, can leverage various features such as crop recommendations, crop yield prediction, "
            "and access to best farming practices. Below is an overview of the available endpoints and their functionalities."
        ),
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    #permission_classes=[IsAuthenticated],
)

    

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/crop/recommender/', include('recommender.urls')),
    path('api/v1/crop/yield/', include('crop_yield.urls')),
    path('api/v1/docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
