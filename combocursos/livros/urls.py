from django.urls import path
from .views import NovoLivro
from .views import ListarLivro
from .views import EditarLivro
from .views import DeletarLivro

urlpatterns = [
    path('novolivro/', NovoLivro.as_view(), name='novolivro'),
    path('listarlivros/', ListarLivro.as_view(), name='listarlivros'),
    path('editarlivro/<int:pk>', EditarLivro.as_view(), name='editarlivro'),
    path('deletarlivro/<int:pk>', DeletarLivro.as_view(), name='deletarlivro'),
]
