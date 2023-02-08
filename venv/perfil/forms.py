from django import forms
from . import models
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha'
    )
    
    def __init__(self, usuario=None, *args, **kwargs):
        return super().__init__(*args, **kwargs)

        self.usuario = usuario
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

        