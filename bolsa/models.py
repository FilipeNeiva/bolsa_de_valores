from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nome

class Acao(models.Model):
    sigla = models.CharField(max_length=5, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresa_Acao')
    data_inicio = models.DateField()

    def __str__(self):
        return self.sigla

class Cotacao(models.Model):
    data = models.DateField()
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE, related_name='acao_cotacao')
    valor = models.FloatField()