# Generated by Django 4.1.3 on 2022-11-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_minicurso_aluno_minicursos'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='minicursos',
            field=models.ManyToManyField(blank=True, null=True, to='main.minicurso'),
        ),
    ]