from django.db import migrations

def inserir_dados_salas(apps, schema_editor):
    import pandas as pd

    df = pd.read_excel(r"C:\Users\Jihad\Desktop\projetos\dados\turmas_salas_docentes_2023_1.xlsb",sheet_name=' turmas sistema atual')
    df = df[['CÓDIGO DE TURMA', 'TURMA', 'Horário Teoria', 'Horário Prática','TPI','Docente Teoria','Docente Prática']]
    
    sala = apps.get_model('calendarioapp', 'Salas')
    for i, dados in df.iterrows():
        sala.objects.create(
            cod=dados['CÓDIGO DE TURMA'],
            turma=dados['TURMA'],
            horarios_teoria=dados['Horário Teoria'],
            horarios_pratica=dados['Horário Prática'],
            tpi=dados['TPI'],
            docente_teoria=dados['Docente Teoria'],
            docente_pratica=dados['Docente Prática']
            )

class Migration(migrations.Migration):
    dependencies = [
        ('calendarioapp', '0003_salas'),
    ]
    operations = [
        migrations.RunPython(inserir_dados_salas),
    ]