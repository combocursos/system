from django.contrib import admin
from django.urls import path, include
from .views import MatricularAluno
from .views import EditarMatricular
from .views import RemoverMatricula

urlpatterns = [
    path('matricularaluno/<int:pk>',
         MatricularAluno.as_view(), name='matricularaluno'),
    path('editarmatricula/<int:pk>',
         EditarMatricular.as_view(), name='editarmatricula'),
    path('removermatricula/<int:pk>',
         RemoverMatricula.as_view(), name='removermatricula'),
]
