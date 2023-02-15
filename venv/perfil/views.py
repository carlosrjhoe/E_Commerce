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

        # self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.filter(
                usuario=self.request.user
            ).first()
            
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None, 
                    usuario=self.request.user,
                    instance=self.request.user
                ),
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None,
                ),
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(data=self.request.POST or None),
                'perfilform': forms.PerfilForm(data=self.request.POST or None),
            }

        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']
        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar


class Criar(BasePerfil):
    def post(self, *args, **kwargs):
        print(self.perfil)
        if not self.userform.is_valid() or not self.userform.is_valid():
            print('INVÁLIDO')
        return self.renderizar

    
class Atualizar(View):
    pass


class Login(View):
    pass


class Logout(View):
    pass
