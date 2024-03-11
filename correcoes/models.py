from django.db import models
from usuarios.models import CustomUser
from core.models import Gasto

class Correcao(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return f"Correção de {self.gasto.nome} por {self.usuario.username}"