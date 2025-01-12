"""
URL configuration for emmerce_crm_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.conf import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Emmerce Mini CRM API",
        default_version='v1',
        description="This is a system that is used to help agents track their leads.",
        terms_of_service="",
        contact=openapi.Contact(email="etolejames@gmail.com"),
        license=openapi.License(name="MIT Lisense."),
    ),
    public=True,
    authentication_classes=[],
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/', include('emmerce_crm_backend.apps.authentication.urls')),
    path('api/leads/', include('emmerce_crm_backend.apps.leads.urls')),
    path('api/contacts/', include('emmerce_crm_backend.apps.contacts.urls')),
    path('api/notes/', include('emmerce_crm_backend.apps.notes.urls')),
    path('api/reminders/', include('emmerce_crm_backend.apps.reminders.urls')),
]

