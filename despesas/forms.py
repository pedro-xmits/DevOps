from django import forms
from .models import Despesa

class despesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ('nome', 'descricao')