from django.shortcuts import render
from calendarioapp.models import HorarioAula, TurmaPorRA, Salas

# Create your views here.
def index(request):
    if 'ra' in request.GET:
        ra = request.GET['ra']
        materias = TurmaPorRA.objects.filter(ra=ra)

        q1seg_8 = ''
        q1seg_10 = ''
        q1seg_14 = ''
        q1seg_16 = ''
        q1seg_19 = ''
        q1seg_21 = ''
        q2seg_8 = ''
        q2seg_10 = ''
        q2seg_14 = ''
        q2seg_16 = ''
        q2seg_19 = ''
        q2seg_21 = ''
        

        for materia in materias:
            infos = Salas.objects.filter(cod=materia.codigo_turma)
            for info in infos:
                dias = [info.dia1, info.dia2, info.dia3, info.dia4, info.dia5, info.dia6]
                horarios = [info.horario1, info.horario2 , info.horario3, info.horario4, info.horario5, info.horario6]
                salas = [info.sala1, info.sala2 , info.sala3, info.sala4, info.sala5, info.sala6]
                frequencias = [info.frequencia1, info.frequencia2 , info.frequencia3, info.frequencia4, info.frequencia5, info.frequencia6]
                
                for dia,horario,sala,frequencia in zip(dias,horarios,salas,frequencias):
                    dias_for = ['segunda', 'terça', 'quarta', 'quinta', 'sexta']
                    for dia_for in dia_for:
                        if dia == dia_for:
                            if horario == "08:00":
                                #ajustar as variaveis, usar o vars()[dia] , declarar tudo antes para n dar erro, otimizar a declaração
                                if frequencia == 'quinzenal I':
                                    q1seg_8 = info.turma + dia + sala
                                elif frequencia == 'quinzenal II':
                                    q2seg_8 = info.turma + dia + sala
                                else:
                                    q1seg_8 = info.turma + dia + sala
                                    q2seg_8 = info.turma + dia + sala

                            if horario == "10:00":
                                if frequencia == 'quinzenal I':
                                    q1seg_10 = info.turma + dia + sala
                                elif frequencia == 'quinzenal II':
                                    q2seg_10 = info.turma + dia + sala
                                else:
                                    q1seg_10 = info.turma + dia + sala
                                    q2seg_10 = info.turma + dia + sala

                            if horario == "14:00":
                                if frequencia == 'quinzenal I':
                                    q1seg_14 = info.turma + dia + sala
                                elif frequencia == 'quinzenal II':
                                    q2seg_14 = info.turma + dia + sala
                                else:
                                    q1seg_14 = info.turma + dia + sala
                                    q2seg_14 = info.turma + dia + sala

                            if horario == "16:00":
                                if frequencia == 'quinzenal I':
                                    q1seg_16 = info.turma + dia + sala
                                elif frequencia == 'quinzenal II':
                                    q2seg_16 = info.turma + dia + sala
                                else:
                                    q1seg_16 = info.turma + dia + sala
                                    q2seg_16 = info.turma + dia + sala

                            if horario == "19:00":
                                if frequencia == 'quinzenal I':
                                    q1seg_19 = info.turma + dia + sala
                                elif frequencia == 'quinzenal II':
                                    q2seg_19 = info.turma + dia + sala
                                else:
                                    q1seg_19 = info.turma + dia + sala
                                    q2seg_19 = info.turma + dia + sala

                            if horario == "21:00":
                                if frequencia == 'quinzenal I':
                                    q1seg_21 = info.turma + dia + sala
                                elif frequencia == 'quinzenal II':
                                    q2seg_21 = info.turma + dia + sala
                                else:
                                    q1seg_21 = info.turma + dia + sala
                                    q2seg_21 = info.turma + dia + sala

                        
                        dados = {
                            "q1seg_08": q1seg_8,
                            "q1seg_10": q1seg_10,
                            "q1seg_14": q1seg_14,
                            "q1seg_16": q1seg_16,
                            "q1seg_19": q1seg_19,
                            "q1seg_21": q1seg_21,
                            "q2seg_08": q2seg_8,
                            "q2seg_10": q2seg_10,
                            "q2seg_14": q2seg_14,
                            "q2seg_16": q2seg_16,
                            "q2seg_19": q2seg_19,
                            "q2seg_21": q2seg_21,
                            # preencha mais informações aqui
                        }

    else:
        dados = None

    return render(request, 'calendario/index.html',dados)

