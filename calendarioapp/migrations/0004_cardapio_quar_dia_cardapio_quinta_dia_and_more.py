# Generated by Django 4.1.7 on 2023-03-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarioapp', '0003_cardapio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardapio',
            name='quar_dia',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='cardapio',
            name='quinta_dia',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='cardapio',
            name='seg_dia',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='cardapio',
            name='sexta_dia',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='cardapio',
            name='ter_dia',
            field=models.CharField(default='', max_length=250),
        ),
    ]
