from django import forms
from .models import Gasto

class gastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ('nome', 'valor', 'tipo','data')
        widgets = {
            'data': forms.SelectDateWidget()
        }