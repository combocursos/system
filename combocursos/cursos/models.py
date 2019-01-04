from django.db import models

# Create your models here.


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    periodo = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
