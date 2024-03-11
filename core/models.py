from django.db import models
from despesas.models import Despesa
from usuarios.models import CustomUser

class Gasto(models.Model):
    nome = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    tipo = models.ForeignKey(Despesa, on_delete=models.CASCADE)
    data = models.DateField()
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
         return self.nome


