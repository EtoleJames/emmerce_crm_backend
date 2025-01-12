from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

app_name = 'contacts'

router = DefaultRouter()
router.register(r'', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]