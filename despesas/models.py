from django.db import models

class Despesa(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)

    def __str__(self):
         return self.nome