from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    data_nascimento = models.DateField(null=True, default=None)
    data_matricula = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    
class Aula(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    curso = models.IntegerField(choices=[(1, 'Desenvolvimento Full-Stack'), (2, 'Desenvolvimento Front-End'), (3, 'Python'), (4, 'SQL'), (5, 'HTML'), (5,'Javascript')])   