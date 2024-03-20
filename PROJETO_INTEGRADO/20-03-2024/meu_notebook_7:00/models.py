from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    data_nascimento = models.DateField(null=True, default=None)
    data_matricula = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

class Professor(models.Model):
    especialidade = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    
class Aula(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    conteudo = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
    
'''
class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel_dificuldade = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateField(auto_now_add=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='cursos')
    alunos = models.ManyToManyField(Aluno, related_name='cursos')
'''