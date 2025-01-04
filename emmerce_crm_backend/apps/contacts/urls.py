from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

router = DefaultRouter()
router.register(r'', ContactViewSet, basename='/')

urlpatterns = [
    path('', include(router.urls)),
]