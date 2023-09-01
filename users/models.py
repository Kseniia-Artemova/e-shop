from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='E-mail')

    avatar = models.ImageField(blank=True, null=True, upload_to='users/', default='users/anonim.jpg', verbose_name='Аватар')
    phone = models.CharField(blank=True, null=True, max_length=60, verbose_name='Телефон')
    country = models.CharField(blank=True, null=True, max_length=60, verbose_name='Страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

