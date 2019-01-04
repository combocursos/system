from django.db import models
from cursos.models import Curso

# Create your models here.


class Dia(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Turno(models.Model):
    nome = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Horario(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Matricula(models.Model):

    STATUS_CHOICES = (
        ('Estudando', 'Estudando'),
        ('Desistente', 'Desistente'),
        ('Em Pausa', 'Em Pausa'),
        ('Concluido', 'Concluido'),
    )

    aluno = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    data_matricula = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_termino = models.BooleanField(default=False)
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, default='Estudando')
    pagamento = models.CharField(max_length=50)
    horario = models.ForeignKey('Horario', on_delete=models.CASCADE)
    turno = models.ForeignKey('Turno', on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dia = models.ForeignKey('Dia', on_delete=models.CASCADE)

    def __str__(self):
        return self.aluno.nome
