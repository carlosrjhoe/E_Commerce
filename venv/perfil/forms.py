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
    password_2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmação da Senha'
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
        validation_error_msg = {}

        usuario_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = 'Usuário já existe.'
        error_msg_email_exists = 'E-mail já existe.'
        error_msg_password_match = 'As duas senhas não conferem.'
        error_msg_password_short = 'Sua senha precisa ter 6 caracteres...'

        if self.usuario:
            if usuario_data != usuario_db.username:
                if usuario_db:
                    validation_error_msg['username'] = error_msg_user_exists
                    
                if email_data != email_db.email:
                    validation_error_msg['email'] = error_msg_email_exists
                    
                if password_data:
                    if password_data != password2_data:
                        validation_error_msg['password'] = error_msg_password_match
                        validation_error_msg['password2'] = error_msg_password_match
                    if len(password_data):
                        if email_db:
                            validation_error_msg['password'] = error_msg_password_short
        else:
            pass

        if validation_error_msg:
            raise(forms.ValidationError(validation_error_msg))
        else:
            pass