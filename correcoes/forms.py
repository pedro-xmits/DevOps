from django import forms
from .models import Correcao
from usuarios.models import CustomUser
from core.models import Gasto
from django.http import request

class CorrecaoForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=CustomUser.objects.all(), label='Selecione o usuário')
    gasto = forms.ModelChoiceField(queryset=Gasto.objects, label='Selecione o gasto irregular')

    class Meta:
        model = Correcao
        fields = ['usuario', 'gasto', 'descricao']