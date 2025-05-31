from django.db import models

# Create your models here.
class ClientesModel(models.Model): 

 GENEROS = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outro'),
    ]


 nome = models.CharField(max_length=100)
 genero = models.CharField(max_length=1, choices=GENEROS)
 idade = models.PositiveIntegerField()
 email = models.EmailField(unique=True)
 telefone = models.CharField(max_length=15)
 data_inscricao = models.DateField(auto_now_add=True)
 plano = models.CharField(max_length=50)

def __str__(self):
        return self.nome

class RelatorioDesempenho(models.Model):
    ESTACOES = [('Verão', 'Verão'), ('Outono', 'Outono'), ('Inverno', 'Inverno'), ('Primavera', 'Primavera')]

    cliente = models.ForeignKey(ClientesModel, on_delete=models.CASCADE)
    frequencia = models.IntegerField(help_text="Dias de treino por semana")
    estacao = models.CharField(max_length=10, choices=ESTACOES)
    objetivo_alcancado = models.BooleanField()
    satisfacao = models.IntegerField(help_text="Nota de 0 a 10")
    lesoes = models.BooleanField()
    chance_desistencia = models.FloatField(null=True, blank=True)  
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Relatório de {self.cliente.nome} - {self.data}"