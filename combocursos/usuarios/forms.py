from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario, Tipo, Cidade, Bairro
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect, render, render_to_response
from django.utils import timezone


class UsuarioCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username',
                  'nome',
                  'data_nascimento',
                  'cpf',
                  'rg',
                  'endereco',
                  'responsavel',
                  'telefone_responsavel',
                  'cpf_responsavel',
                  'observacoes',
                  'telefone',
                  'tipo',
                  )

    def clean_cpf(self):
        if self.cleaned_data['cpf'] == "" or None:
            return None
        else:
            return self.cleaned_data['cpf']


class UsuarioChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = UserChangeForm.Meta.fields


# Aluno Forms
class AlunoCreationForm(UserCreationForm):
    tipo = forms.ModelChoiceField(queryset=Tipo.objects.filter(
        id=1), initial=1, widget=forms.HiddenInput())
    cidade = forms.ModelChoiceField(
        queryset=Cidade.objects.all(), initial='Cidade')
    bairro = forms.ModelChoiceField(
        queryset=Bairro.objects.all(), initial='Bairro')

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username',
                  'nome',
                  'data_nascimento',
                  'cpf',
                  'rg',
                  'responsavel',
                  'telefone_responsavel',
                  'cpf_responsavel',
                  'observacoes',
                  'telefone',
                  'tipo',
                  'endereco',
                  'cidade',
                  'bairro',
                  'date_joined',
                  )

    def clean_cpf(self):
        if self.cleaned_data['cpf'] == "" or None:
            return None
        else:
            return self.cleaned_data['cpf']


class AlunoChangeForm(UserChangeForm):
    tipo = forms.ModelChoiceField(queryset=Tipo.objects.filter(
        id=1), initial=1, widget=forms.HiddenInput())

    class Meta:
        model = Usuario
        fields = UserChangeForm.Meta.fields


# Funcionários Forms
class FuncionarioCreationForm(UserCreationForm):
    cidade = forms.ModelChoiceField(queryset=Cidade.objects.all(),)
    bairro = forms.ModelChoiceField(queryset=Bairro.objects.all(),)
    tipo = forms.ModelChoiceField(
        queryset=Tipo.objects.all().exclude(id=1), initial=2,)

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username',
                  'nome',
                  'data_nascimento',
                  'cpf',
                  'rg',
                  'endereco',
                  'cidade',
                  'bairro',
                  'telefone',
                  'tipo',
                  )


class FuncionarioChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = FuncionarioCreationForm.Meta.fields
