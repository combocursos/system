from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Curso
from .forms import CursoForm


class NovoCurso(CreateView):
    model = Curso
    template_name = 'cursos/novocurso.html'
    form_class = CursoForm

    def get_success_url(self):
        return reverse_lazy("listarcursos")


class ListarCursos(ListView):
    model = Curso
    template_name = 'cursos/listarcursos.html'
    context_object_name = 'cursos'


class EditarCurso(UpdateView):
    model = Curso
    template_name = 'cursos/novocurso.html'
    form_class = CursoForm

    def get_success_url(self):
        return reverse_lazy("listarcursos")


class DeletarCurso(DeleteView):
    model = Curso

    def get_success_url(self):
        return reverse_lazy("listarcursos")
