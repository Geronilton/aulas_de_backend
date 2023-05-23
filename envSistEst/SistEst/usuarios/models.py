from django.db import models

# Create your models here.

class Usuarios(models.Model):
    idUsuario = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length = 300,null=False)
    cpf = models.CharField(max_length=11, null=False)
    num_CNH = models.CharField(max_length=15,null=True)
    validade_CNH = models.DateField(null=True, help_text="Formato <em>YYYT-MM-DD </em>")
    telefone = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=300,null=True)

    class Meta:
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.cpf + " - " + self.nome

class Carros(models.Model):
    idCarro = models.BigAutoField(primary_key=True)
    placa = models.CharField(max_length=10, null=False)
    marca_modelo = models.CharField(max_length=300, null=False)
    cor = models.CharField(max_length=50,null=False)
    fk_idUsuario = models.ForeignKey(Usuarios,on_delete= models.CASCADE)

    class Meta:
        verbose_name_plural = "Carros"

    def __str__(self):
        return self.placa

class Estacionamentos(models.Model):
    idEstacionamento= models.BigAutoField(primary_key=True)
    data_entrada = models.DateField(auto_now_add=True, null=False,
                    help_text="Formato <em>YYYT-MM-DD </em>")
    hora_entrada = models.TimeField(auto_now_add=True,null=False,
                    help_text="Formato <em>YYYT-MM-DD </em>")
    data_saida = models.DateField(null=True,blank=True,
                    help_text="Formato <em>YYYT-MM-DD </em>")
    hora_saida = models.TimeField(null=True,blank=True,
                    help_text="Formato <em>YYYT-MM-DD </em>")
    fk_idCarro = models.ForeignKey(Carros,on_delete=models.CASCADE, verbose_name="Placa do Carro")

    class Meta:
        verbose_name_plural = "Estacionamentos"

    def __str__(self):
        return self.data_entrada.strftime("%Y/%m/%d") +" - " + self.hora_entrada.strftime("%H:%M:%S")