from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from . import models
from . import forms


# Create your views here.
class BasePerfil(View):
    template_name = 'perfil/criar.html'
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.contexto = {
            'userform': forms.UserForm(data=self.request.POST or None),
            'perfilform': forms.PerfilForm(data=self.request.POST or None),
        }

        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar

class Criar(BasePerfil):
    pass

class Atualizar(View):
    pass

class Login(View):
    pass

class Logout(View):
    pass


