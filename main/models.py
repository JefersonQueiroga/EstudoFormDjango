from django.db import models

LISTA_SEXO= [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
]

class MiniCurso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    data_nascimento = models.DateTimeField()
    sexo = models.CharField(max_length=150,choices=LISTA_SEXO,default='Feminino')
    minicursos = models.ManyToManyField(MiniCurso)

    def __str__(self) -> str:
        return self.nome