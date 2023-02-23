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
