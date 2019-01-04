from django.db import models

# Modelos Primários


# class Livro(models.Model):
#     nome = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome


# # Modelos Compostos
# class Turma(models.Model):
#     dia = models.ForeignKey('Dia', on_delete=models.CASCADE)
#     horario = models.ForeignKey('Horario', on_delete=models.CASCADE)
#     turno = models.ForeignKey('Turno', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.dia.nome


# class ProfessorTurma(models.Model):
#     curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
#     turma = models.ForeignKey('Turma', on_delete=models.CASCADE)
#     professor = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.curso.nome


# class Modulo(models.Model):
#     nome = models.CharField(max_length=150)
#     curso = models.ForeignKey('Curso', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nome


# class Frequencia(models.Model):
#     status = models.BooleanField(default=False)
#     data = models.DateField(default=timezone.now)
#     aluno = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
#     curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
