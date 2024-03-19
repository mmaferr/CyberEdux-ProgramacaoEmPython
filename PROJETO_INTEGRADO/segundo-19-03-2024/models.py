from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_matricula = models.DateField(auto_now_add=True)

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel_dificuldade = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateField(auto_now_add=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='cursos')
    alunos = models.ManyToManyField(Aluno, related_name='cursos')

class Avaliacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
