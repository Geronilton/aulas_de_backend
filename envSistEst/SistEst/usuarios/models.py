from django.db import models

# Create your models here.

class Usuarios(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length = 300,null=False)
    cpf = models.CharField(max_length=11, null=False)
    num_CNH = models.CharField(max_length=15,null=True)
    validade_CNH = models.DateField(null=True, help_text="Formato <em>YYYT-MM-DD </em>")
    telefone = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=300,null=True)


    def __str__(self):
        return self.cpf + " - " + self.nome