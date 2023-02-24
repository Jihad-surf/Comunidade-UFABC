# Generated by Django 4.1.6 on 2023-02-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarioapp', '0002_inserir_dadosRaTurma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=30)),
                ('turma', models.CharField(max_length=100)),
                ('horarios_teoria', models.CharField(max_length=250)),
                ('horarios_pratica', models.CharField(max_length=250)),
                ('tpi', models.CharField(max_length=20)),
                ('docente_teoria', models.CharField(max_length=100)),
                ('docente_pratica', models.CharField(max_length=100)),
            ],
        ),
    ]
