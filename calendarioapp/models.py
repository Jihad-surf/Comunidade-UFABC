from django.db import models

# Create your models here.

class HorarioAula(models.Model):
    DIA_SEMANA_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    horario = models.CharField(max_length=2)
    dia_semana = models.CharField(max_length=10, choices=DIA_SEMANA_CHOICES)
    materia = models.CharField(max_length=50, blank=True)
    cor = models.CharField(max_length=10, blank=True)

class TurmaPorRA(models.Model):
    ra = models.CharField(max_length=15)
    codigo_turma = models.CharField(max_length=25)

class Salas(models.Model):
    cod = models.CharField(max_length=30)
    turma = models.CharField(max_length=100)
    tpi = models.CharField(max_length=20)
    docente_teoria = models.CharField(max_length=100)
    docente_pratica = models.CharField(max_length=100)
    dia1=models.CharField(max_length=30,default='')
    horario1=models.CharField(max_length=30, default='')
    horario1_fim=models.CharField(max_length=30, default='')
    sala1=models.CharField(max_length=30, default='')
    frequencia1=models.CharField(max_length=30, default='')

    dia2=models.CharField(max_length=30, default='')
    horario2=models.CharField(max_length=30, default='')
    horario2_fim=models.CharField(max_length=30, default='')
    sala2=models.CharField(max_length=30, default='')
    frequencia2=models.CharField(max_length=30, default='')

    dia3=models.CharField(max_length=30, default='')
    horario3=models.CharField(max_length=30, default='')
    horario3_fim=models.CharField(max_length=30, default='')
    sala3=models.CharField(max_length=30, default='')
    frequencia3=models.CharField(max_length=30, default='')

    dia4=models.CharField(max_length=30, default='')
    horario4=models.CharField(max_length=30, default='' )
    horario4_fim=models.CharField(max_length=30, default='')
    sala4=models.CharField(max_length=30, default='')
    frequencia4=models.CharField(max_length=30 , default='')

    dia5=models.CharField(max_length=30, default='')
    horario5=models.CharField(max_length=30, default='')
    horario5_fim=models.CharField(max_length=30, default='')
    sala5=models.CharField(max_length=30, default='')
    frequencia5=models.CharField(max_length=30, default='')

    dia6=models.CharField(max_length=30, default='')
    horario6=models.CharField(max_length=30, default='')
    horario6_fim=models.CharField(max_length=30, default='')
    sala6=models.CharField(max_length=30, default='')
    frequencia6=models.CharField(max_length=30, default='')
