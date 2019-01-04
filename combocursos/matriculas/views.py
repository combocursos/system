from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import View
from django.views.generic import RedirectView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from usuarios.models import Usuario
from usuarios.forms import AlunoChangeForm
from .models import Matricula
from .forms import MatriculaForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from usuarios.forms import AlunoCreationForm
from usuarios.forms import FuncionarioCreationForm
from usuarios.forms import FuncionarioChangeForm

# Create your views here.


class MatricularAluno(DetailView, CreateView):
    model = Matricula
    form_class = MatriculaForm
    queryset = Usuario.objects.filter(tipo=1)
    template_name = "matriculas/matricularaluno.html"
    context_object_name = "aluno"

    def get_success_url(self, **kwargs):
        return reverse_lazy("perfil", args=(self.object.aluno.id,))


class EditarMatricular(UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = "matriculas/editarmatricula.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy("perfil", args=(self.object.aluno.id,))


class RemoverMatricula(DeleteView):
    model = Matricula

    def get_success_url(self, **kwargs):
        return reverse_lazy("perfil", args=(self.object.aluno.id,))
