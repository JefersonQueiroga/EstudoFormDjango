from django.db import models

# Create your models here.


class Questao(models.Model):
    descricao = models.CharField(max_length=300)


class Opcao(models.Model):
    descricao = models.CharField(max_length=300)
    questao = models.ForeignKey(Questao,on_delete=models.PROTECT,related_name='opcoes')