from django.shortcuts import render
from calendarioapp.models import HorarioAula, TurmaPorRA

# Create your views here.
def index(request):
    if 'ra' in request.GET:
        ra = request.GET['ra']
        aulas = TurmaPorRA.objects.filter(ra=ra)
        
        #dados = HorarioAula
        for aula in aulas:
            print(aula.codigo_turma)

    return render(request, 'calendario/index.html')

