from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Livro
from .forms import LivroForm


class NovoLivro(CreateView):
    model = Livro
    template_name = 'livros/novolivro.html'
    form_class = LivroForm

    def get_success_url(self):
        return reverse_lazy("listarlivros")


class ListarLivro(ListView):
    model = Livro
    template_name = 'livros/listarlivros.html'
    context_object_name = 'livros'


class EditarLivro(UpdateView):
    model = Livro
    template_name = 'livros/novolivro.html'
    form_class = LivroForm

    def get_success_url(self):
        return reverse_lazy("listarlivros")


class DeletarLivro(DeleteView):
    model = Livro

    def get_success_url(self):
        return reverse_lazy("listarlivros")
