from calendarioapp.models import TurmaPorRA
from PyPDF2 import PdfReader


def run():
    with open(r"C:\Users\Jihad\Desktop\projetos\dados\ajuste_2023_1_deferidos_pos_ajuste.pdf", 'rb') as f:
        pdf = PdfReader(f)
        texto_completo = ''
        for pagina in pdf.pages:
            texto_completo += pagina.extract_text()

    with open(r"C:\Users\Jihad\Desktop\projetos\dados\reajuste_2023_01_matriculas_deferidas.pdf", 'rb') as f:
        pdf = PdfReader(f)
        for pagina in pdf.pages:
            texto_completo += pagina.extract_text()

    # Extrair as informações das colunas de interesse
    coluna_ra = []
    coluna_turma = []
    for linha in texto_completo.split('\n'):
        if len(linha) < 30 or 'MATRÍCULAS' in linha or 'MATRICULAS' in linha:
            continue
        campos = linha.split()
        coluna_ra.append(campos[0])
        coluna_turma.append(campos[1])
   
    TurmaPorRA.objects.all().delete()
    for ra, turma in zip(coluna_ra, coluna_turma):
        TurmaPorRA.objects.create(ra=ra, codigo_turma=turma)

