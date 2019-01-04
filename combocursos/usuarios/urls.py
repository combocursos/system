from django.contrib import admin
from django.urls import path, include
from .views import NovoAluno
from .views import ListarAlunos
from .views import EditarAluno
from .views import ExcluirAluno
from .views import NovoFuncionario
from .views import ListarFuncionarios
from .views import ExcluirFuncionario
from .views import EditarFuncionario

urlpatterns = [
    path('novoaluno/', NovoAluno.as_view(), name='novoaluno'),
    path('listaralunos/', ListarAlunos.as_view(), name='listaralunos'),
    path('editaraluno/<int:pk>', EditarAluno.as_view(), name='editaraluno'),
    path('excluiraluno/<int:pk>', ExcluirAluno.as_view(), name='excluiraluno'),
    path('novofuncionario/', NovoFuncionario.as_view(), name='novofuncionario'),
    path('listarfuncionarios/', ListarFuncionarios.as_view(),
         name='listarfuncionarios'),
    path('excluirfuncionario/<int:pk>',
         ExcluirFuncionario.as_view(), name='excluirfuncionario'),
    path('editarfuncionario/<int:pk>',
         EditarFuncionario.as_view(), name='editarfuncionario'),
]
