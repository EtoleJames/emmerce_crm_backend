from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(_('Email address'), blank=True, unique=True)
    phone = models.CharField(_('Phone Number'), max_length=50, blank=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']