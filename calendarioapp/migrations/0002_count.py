# Generated by Django 4.1.7 on 2023-03-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarioapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, unique=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
