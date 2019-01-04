from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Este model está restrito apenas a usuários e seus endereçamentos.

# Other Models


class Tipo(models.Model):
    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Bairro(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

# End Other Models

# Usuarios Model


class Usuario(AbstractUser):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    telefone_responsavel = models.CharField(max_length=11)
    cpf_responsavel = models.CharField(max_length=11)
    observacoes = models.TextField()
    telefone = models.CharField(max_length=11)
    tipo = models.ForeignKey(
        'Tipo', null=True, blank=True, on_delete=models.CASCADE)
    cidade = models.ForeignKey(
        'Cidade', null=True, blank=True, on_delete=models.CASCADE)
    bairro = models.ForeignKey(
        'Bairro', null=True, blank=True, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    class Meta:
        verbose_name = "Usuario"

    def __str__(self):
        return self.username
