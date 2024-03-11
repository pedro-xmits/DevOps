from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    TIPO_CHOICES=(('VE', 'Vendedor'), ('CE','Corretor'), ('AD', 'Administrador'))

    regiao = models.CharField(max_length=10)
    cargo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default='VE')
    first_name = models.CharField(verbose_name='Nome')
    last_name = models.CharField(verbose_name='Sobrenome')
