from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    cpf = models.CharField('cpf', max_length=11, unique=True)
    nome_completo = models.CharField('Nome Completo', max_length=30, null=True)
    data_nascimento = models.DateField('Data de Nascimento', null=True)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['username']

    class Meta:
        permissions = [
            ('bibliotecario','Permissão do Usuario Bibliotecario'),
            ('coordenador','Permissão do Usuario Coordenador')
        ]

class Area(models.Model):
    nome = models.CharField('Nome', max_length=20)
    def __str__(self):
        return self.nome

class Publico(models.Model):
    nome= models.CharField('Nome', max_length=30)

    def __str__(self):
        return self.nome

class curso(models.Model):
    titulo = models.CharField('titulo', max_length=100)
    vagas = models.IntegerField('vagas')
    data_inicio = models.DateField('Data de Inicio')
    data_criacao = models.DateField('Data de Criação', auto_now_add= True)
    data_modificacao = models.DateField('Data de Modificação', auto_now=True)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publico = models.ManyToManyField(Publico)