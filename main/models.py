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
    cpf = models.CharField(max_length=20)
    sexo = models.CharField(max_length=150,choices=LISTA_SEXO)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateTimeField()
    minicursos = models.ManyToManyField(MiniCurso, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome