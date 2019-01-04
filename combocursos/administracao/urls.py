from django.contrib import admin
from django.urls import path, include
from .views import PerfilAluno
from .views import PerfilFuncionario
from .views import Home
from .views import HomeSelect
from .views import DashBoard
from .views import Perfil
from .views import AlunoDashboard
from .views import ProfessorDashboard
from .views import FuncionarioDashboard

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('homeselect', HomeSelect.as_view(), name='homeselect'),
    path('dashboard/', DashBoard.as_view(), name='dashboard'),
    path('perfil/<int:pk>', Perfil.as_view(), name='perfil'),
    path('alunodashboard/', AlunoDashboard.as_view(), name='alunodashboard'),
    path('professordashboard/', ProfessorDashboard.as_view(),
         name='professordashboard'),
    path('funcionariodashboard/', FuncionarioDashboard.as_view(),
         name='funcionariodashboard'),
    path('perfilaluno/<int:pk>', PerfilAluno.as_view(), name='perfilaluno'),
    path('perfilfuncionario/<int:pk>',
         PerfilFuncionario.as_view(), name='perfilfuncionario'),
]
