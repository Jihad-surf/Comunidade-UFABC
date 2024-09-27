import pandas as pd
from calendarioapp.models import Salas

def run():

    df = pd.read_excel(r"C:\Users\Jihad\Desktop\projetos\dados\aulas202401.xlsx",sheet_name='Planilha2')
    df = df[['CÓDIGO DE TURMA', 'TURMA', 'Horário Teoria', 'Horário Prática','TPI','Docente Teoria','Docente Prática']]
 
    novas_colunas = pd.DataFrame(columns=['dia1', 'horario1','horario1_fim', 'sala1', 'frequencia1',
                                      'dia2', 'horario2','horario2_fim', 'sala2', 'frequencia2',
                                      'dia3', 'horario3','horario3_fim', 'sala3', 'frequencia3',
                                      'dia4', 'horario4','horario4_fim', 'sala4', 'frequencia4',
                                      'dia5', 'horario5','horario5_fim', 'sala5', 'frequencia5',
                                      'dia6', 'horario6','horario6_fim', 'sala6', 'frequencia6'])
    df = df.join(novas_colunas)

    df.fillna('', inplace=True)
    df['Horário Teoria'] = df['Horário Teoria'].str.replace('\n',' ')
    i = 0
    for dados in df['Horário Teoria']:
        dados = dados.split(', ')
        if len(dados)>=2:
            df.loc[i, 'dia1'] = dados[0].split()[0]
            df.loc[i, 'horario1'] = dados[0].split()[2]
            df.loc[i, 'horario1_fim'] = dados[0].split()[4]

            if len(dados[1].replace(' ', '').split('sala')) == 1:
                df.loc[i, 'sala1'] = dados[1].replace(' ', '').split('sala')[0]
            else:
                df.loc[i, 'sala1'] = dados[1].replace(' ', '').split('sala')[1]
            df.loc[i, 'frequencia1'] = dados[2]

        if len(dados)>=5:
            df.loc[i, 'dia2'] = dados[3].split()[0]
            df.loc[i, 'horario2'] = dados[3].split()[2]
            df.loc[i, 'horario2_fim'] = dados[3].split()[4]
            if len(dados[4].replace(' ', '').split('sala')) == 1:
                df.loc[i, 'sala2'] = dados[4].replace(' ', '').split('sala')[0]
            else:
                df.loc[i, 'sala2'] = dados[4].replace(' ', '').split('sala')[1]
            df.loc[i, 'frequencia2'] = dados[5]
            
        if len(dados)>=8:
            df.loc[i, 'dia3'] = dados[6].split()[0]
            df.loc[i, 'horario3'] = dados[6].split()[2]
            df.loc[i, 'horario3_fim'] = dados[6].split()[4]
            df.loc[i, 'sala3'] = dados[7].replace(' ', '').split('sala')[1]
            df.loc[i, 'frequencia3'] = dados[8]
        i += 1

    df['Horário Prática'] = df['Horário Prática'].str.replace('\n',' ')
    
    i = 0
    for dados in df['Horário Prática']:
        dados = dados.split(', ')
        if len(dados)>=2:
            df.loc[i, 'dia4'] = dados[0].split()[0]
            df.loc[i, 'horario4'] = dados[0].split()[2]
            df.loc[i, 'horario4_fim'] = dados[0].split()[4]
            df.loc[i, 'sala4'] = dados[1].replace(' ', '').split('sala')[1]
            df.loc[i, 'frequencia4'] = dados[2]
        if len(dados)>=5:
            df.loc[i, 'dia5'] = dados[3].split()[0]
            df.loc[i, 'horario5'] = dados[3].split()[2]
            df.loc[i, 'horario5_fim'] = dados[3].split()[4]
            df.loc[i, 'sala5'] = dados[4].replace(' ', '').split('sala')[1]
            df.loc[i, 'frequencia5'] = dados[5]
        if len(dados)>=8:
            df.loc[i, 'dia6'] = dados[6].split()[0]
            df.loc[i, 'horario6'] = dados[6].split()[2]
            df.loc[i, 'horario6_fim'] = dados[6].split()[4]
            df.loc[i, 'sala6'] = dados[7].replace(' ', '').split('sala')[1]
            df.loc[i, 'frequencia6'] = dados[8]
        i += 1

    # quando trocar o quad deletar tudo antes
    Salas.objects.all().delete()
    for i, dados in df.iterrows():
        Salas.objects.create(
            cod=dados['CÓDIGO DE TURMA'],
            turma=dados['TURMA'],
            tpi='',
            docente_teoria=dados['Docente Teoria'],
            docente_pratica=dados['Docente Prática'],
            dia1 = dados['dia1'],
            horario1 = dados['horario1'],
            horario1_fim = dados['horario1_fim'],
            sala1 = dados['sala1'],
            frequencia1 = dados['frequencia1'],


            dia2 = dados['dia2'],
            horario2 = dados['horario2'],
            horario2_fim = dados['horario2_fim'],
            sala2 = dados['sala2'],
            frequencia2 = dados['frequencia2'],


            dia3 = dados['dia3'],
            horario3 = dados['horario3'],
            horario3_fim = dados['horario3_fim'],
            sala3 = dados['sala3'],
            frequencia3 = dados['frequencia3'],


            dia4 = dados['dia4'],
            horario4 = dados['horario4'],
            horario4_fim = dados['horario4_fim'],
            sala4 = dados['sala4'],
            frequencia4 = dados['frequencia4'],


            dia5 = dados['dia5'],
            horario5 = dados['horario5'],
            horario5_fim = dados['horario5_fim'],
            sala5 = dados['sala5'],
            frequencia5 = dados['frequencia5'],


            dia6 = dados['dia6'],
            horario6 = dados['horario6'],
            horario6_fim = dados['horario6_fim'],
            sala6 = dados['sala6'],
            frequencia6 = dados['frequencia6']
            )
        