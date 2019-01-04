from django.urls import path
from .views import NovoCurso
from .views import ListarCursos
from .views import EditarCurso
from .views import DeletarCurso

urlpatterns = [
    path('novocurso/', NovoCurso.as_view(), name='novocurso'),
    path('listarcursos/', ListarCursos.as_view(), name='listarcursos'),
    path('editarcurso/<int:pk>', EditarCurso.as_view(), name='editarcurso'),
    path('deletarcurso/<int:pk>', DeletarCurso.as_view(), name='deletarcurso'),
]
