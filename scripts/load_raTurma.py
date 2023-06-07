from calendarioapp.models import TurmaPorRA
from PyPDF2 import PdfReader


def run():
    texto_completo = ''
    with open(r"C:\Users\Jihad\Desktop\projetos\dados\2023_2_matriculas_deferidas_pos_ajuste.pdf", 'rb') as f:
        pdf = PdfReader(f)
        for pagina in pdf.pages:
            texto_completo += pagina.extract_text()
    
    # Extrair as informações das colunas de interesse
    texto_completo = texto_completo.split('21087414')[1]
    coluna_ra = []
    coluna_turma = []
    for linha in texto_completo.split('\n'):
        if len(linha) < 30 or 'MATRÍCULAS' in linha or 'MATRICULAS' in linha:
            continue
        campos = linha.split()
        coluna_ra.append(campos[0])
        coluna_turma.append(campos[1])
   
    #TurmaPorRA.objects.all().delete()
    for ra, turma in zip(coluna_ra, coluna_turma):
        TurmaPorRA.objects.create(ra=ra, codigo_turma=turma)

