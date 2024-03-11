from django.test import TestCase
from .models import Gasto
from despesas.models import Despesa
from usuarios.models import CustomUser
from datetime import date

class GastoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        despesa = Despesa.objects.create(nome='Despesa Teste')
        usuario = CustomUser.objects.create(username='usuario_teste')

        Gasto.objects.create(nome='Gasto Teste', valor=100.00, tipo=despesa, data=date.today(), usuario=usuario)

    def test_str_method(self):
        gasto = Gasto.objects.get(id=1)
        self.assertEqual(gasto.__str__(), 'Gasto Teste')

    def test_valor_field(self):
        gasto = Gasto.objects.get(id=1)
        self.assertEqual(gasto.valor, 100.00)

    def test_tipo_field(self):
        gasto = Gasto.objects.get(id=1)
        self.assertEqual(gasto.tipo.nome, 'Despesa Teste')

    def test_data_field(self):
        gasto = Gasto.objects.get(id=1)
        self.assertEqual(gasto.data, date.today())

    def test_usuario_field(self):
        gasto = Gasto.objects.get(id=1)
        self.assertEqual(gasto.usuario.username, 'usuario_teste')
