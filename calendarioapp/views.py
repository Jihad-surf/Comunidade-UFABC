from django.shortcuts import render
from calendarioapp.models import HorarioAula, TurmaPorRA, Salas

# Create your views here.
def index(request):
    if 'ra' in request.GET:
        ra = request.GET['ra']
        aulas = TurmaPorRA.objects.filter(ra=ra)
        
        #dados = HorarioAula
        for aula in aulas:
            print(aula.codigo_turma)
            materia = Salas.objects.filter(cod=aula.codigo_turma)
            for info in materia:
                print(info.docente_teoria)
                dados = HorarioAula(
                    horario='08', # exemplo de horário
                    dia_semana='segunda',
                    materia='Matemática',
                    cor='#FF0000', # exemplo de cor em hexadecimal
                )
                dados.save()


                
        dados = HorarioAula.objects.get(pk=1)
    else:
        dados = None

    return render(request, 'calendario/index.html',{'dados' :dados})

