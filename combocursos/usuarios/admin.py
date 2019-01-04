from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import Usuario, Tipo, Cidade, Bairro

class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ['id',
                    'username',
                    'nome',
                    'data_nascimento',
                    'cpf', 
                    'rg',
                    'endereco', 
                    'responsavel',
                    'telefone_responsavel',
                    'cpf_responsavel',
                    'observacoes',
                    'telefone',
                    'tipo',
                    ]

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Tipo)
admin.site.register(Cidade)
admin.site.register(Bairro)