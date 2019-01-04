from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import View
from django.views.generic import RedirectView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from usuarios.models import Usuario
from usuarios.forms import AlunoChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from usuarios.forms import AlunoCreationForm
from usuarios.forms import FuncionarioCreationForm
from usuarios.forms import FuncionarioChangeForm


class NovoAluno(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ""
    template_name = "usuarios/novoaluno.html"
    model = Usuario
    form_class = AlunoCreationForm

    def get_success_url(self):
        g = Group.objects.get(name="Alunos")
        g.user_set.add(self.object)
        return reverse_lazy("dashboard")


class ListarAlunos(ListView):
    model = Usuario
    template_name = "usuarios/listaralunos.html"
    queryset = Usuario.objects.filter(tipo=1)
    context_object_name = "alunos"


class EditarAluno(UpdateView):
    model = Usuario
    form_class = AlunoChangeForm
    template_name = "usuarios/editaraluno.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy("perfil", args=(self.object.id,))


class ExcluirAluno(DeleteView):
    model = Usuario

    def get_success_url(self):
        return reverse_lazy("listaralunos")


# Funcionários


class NovoFuncionario(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ""
    template_name = "usuarios/novofuncionario.html"
    model = Usuario
    form_class = FuncionarioCreationForm

    def get_success_url(self):
        return reverse_lazy("home")


class ListarFuncionarios(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ""
    template_name = "usuarios/listarfuncionarios.html"
    model = Usuario
    queryset = Usuario.objects.all().exclude(tipo=1)
    context_object_name = "funcionario"

    def get_success_url(self):
        return reverse_lazy("home")


class ExcluirFuncionario(DeleteView):
    model = Usuario

    def get_success_url(self):
        return reverse_lazy("listarfuncionarios")


class EditarFuncionario(UpdateView):
    model = Usuario
    form_class = FuncionarioChangeForm
    template_name = "usuarios/editarfuncionario.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy("perfilfuncionario", args=(self.object.id,))
