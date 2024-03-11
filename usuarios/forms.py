from django import forms
from .models import CustomUser

class cadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'regiao', 'tipo', 'cargo']
                  