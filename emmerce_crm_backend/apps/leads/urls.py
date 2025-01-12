from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet

app_name ='leads'

router = DefaultRouter()
router.register(r'', LeadViewSet, basename='lead')

urlpatterns = [
    path('', include(router.urls)),
]
