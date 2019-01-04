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
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from usuarios.forms import AlunoCreationForm
from usuarios.forms import FuncionarioCreationForm
from usuarios.forms import FuncionarioChangeForm
from matriculas.models import Matricula

# Home views


class DashBoard(LoginRequiredMixin, TemplateView):
    model = Usuario
    template_name = 'home/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alunos = Usuario.objects.filter(tipo=1).count()
        matriculas = Matricula.objects.all().count()
        estudando = Matricula.objects.filter(
            status="Estudando").distinct('aluno__id').count()
        pausa = Matricula.objects.filter(status="Em Pausa").count()
        context['contagem_alunos'] = alunos
        context['contagem_matriculas'] = matriculas
        context['contagem_alunos_estudando'] = estudando
        context['contagem_alunos_pausa'] = estudando
        return context


class Home(TemplateView):
    template_name = 'home/landing.html'


class AlunoDashboard(TemplateView):
    model: Usuario
    template_name = 'alunos/dashboard.html'


class ProfessorDashboard(TemplateView):
    model: Usuario
    template_name = 'professores/dashboard.html'


class FuncionarioDashboard(TemplateView):
    model: Usuario
    template_name = 'funcionarios/dashboard.html'


class Perfil(DetailView):
    model = Usuario
    # queryset = Usuario.objects.filter(tipo=1)
    context_object_name = 'aluno'
    template_name = 'home/perfil.html'

    def get(self, request, *args, **kwargs):
        aluno_id = int(kwargs['pk'])
        matricula = Matricula.objects.filter(aluno=aluno_id)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['matricula'] = matricula
        return self.render_to_response(context)


class PerfilAluno(DetailView):
    model = Usuario
    # queryset = Usuario.objects.filter(tipo=1)
    context_object_name = "aluno"
    template_name = "alunos/perfil.html"

    def get(self, request, *args, **kwargs):
        aluno_id = int(kwargs["pk"])
        matricula = Matricula.objects.filter(aluno=aluno_id)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context["matricula"] = matricula
        return self.render_to_response(context)


class PerfilFuncionario(DetailView):
    model = Usuario
    # queryset = Usuario.objects.filter(tipo=1)
    context_object_name = "funcionario"
    template_name = "funcionarios/perfil.html"


class HomeSelect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.tipo is not None:
            if user.tipo.id == 1:
                return 'alunodashboard'
            if user.tipo.id == 2:
                return 'professordashboard'
            if user.tipo.id == 3:
                return 'funcionariodashboard'
        else:
            if user.is_superuser:
                return 'dashboard'
