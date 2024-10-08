from django.shortcuts import render
from calendarioapp.models import Count, TurmaPorRA, Salas, Cardapio
from datetime import date, datetime

# Create your views here.

def semana_atual():
    hoje = date.today().strftime("%d-%m")

    semana1 = ['30-09','01-10','02-10','03-10','04-10','05-10','14-10','15-10','16-10','17-10','18-10','19-10','28-10','29-10','30-10','31-10','01-11','02-11','11-11','12-11','13-11','14-11','15-11','16-11','25-11','26-11','27-11','28-11','29-11','30-11','09-12','10-12','11-12','12-12','13-12','14-12']
    semana2 = ['07-10','08-10','09-10','10-10','11-10','12-10','21-10','22-10','23-10','24-10','25-10','26-10','04-11','05-11','06-11','07-11','08-11','09-11','18-11','19-11','20-11','21-11','22-11','23-11','02-12','03-12','04-12','05-12','06-12','07-12','16-12','17-12','18-12','19-12','20-12','21-12']

    if hoje in semana1:
        return 'semana 1'
    elif hoje in semana2:
        return 'semana 2'
    else:
        return 'I am Lost :/'

def index(request):
    ra=''
    page_view,created  = Count.objects.get_or_create(url=ra)
    dados = {}
    dados['num_visits'] = page_view.count

    dados['semana'] = semana_atual()

    if 'ra' in request.GET:
        ra = request.GET['ra']
        materias = TurmaPorRA.objects.filter(ra=ra)

        page_view.increment_count()

        dados['num_visits'] = page_view.count

        dias_for = ['segunda', 'terça', 'quarta', 'quinta', 'sexta']
        horarios_for =['8', '10','14','16','17','18','19', '21']
        semanas = ['q1','q2']
        colors = ['#fff8bbf8', '#bbc9fff8', '#ceffbbf8', '#fcbbfff8', '#ffbbbbf8', '#bbffbef8', '#ffe7bbf8', '#cececef8']
        
        #declarar variaveis
        for semana in semanas:
            for day in dias_for:
                for time in horarios_for:
                    nome_var = semana+day+"_"+time
                    valor_var = ''
                    dados[nome_var] = valor_var
                    dados[nome_var+'cor'] = valor_var

        i = 0       
        for materia in materias:
            infos = Salas.objects.filter(cod=materia.codigo_turma)
            for info in infos:
                dias = [info.dia1, info.dia2, info.dia3, info.dia4, info.dia5, info.dia6]
                horarios = [info.horario1, info.horario2 , info.horario3, info.horario4, info.horario5, info.horario6]
                horarios_fim = [info.horario1_fim, info.horario2_fim, info.horario3_fim, info.horario4_fim, info.horario5_fim, info.horario6_fim]
                salas = [info.sala1, info.sala2 , info.sala3, info.sala4, info.sala5, info.sala6]
                frequencias = [info.frequencia1, info.frequencia2 , info.frequencia3, info.frequencia4, info.frequencia5, info.frequencia6]
                
                turma = info.turma.replace('Santo André', 'SA')
                turma = turma.replace('São Bernardo do Campo', 'SBC')
                turma = turma.replace('TURMA MINISTRADA EM INGLÊS', 'Ingles')
                turma = turma.replace('-diurno', '')
                turma = turma.replace('-noturno', '')

                for dia,horario, horario_fim,sala,frequencia in zip(dias,horarios, horarios_fim,salas,frequencias):
                    for dia_for in dias_for:
                        if dia == dia_for:
                            if horario == "08:00":
                                #ajustar as variaveis, usar o vars()[dia] , declarar tudo antes para n dar erro, otimizar a declaração
                                if frequencia == 'quinzenal I':
                                    dados['q1'+dia_for+'_8']= turma + ' • ' + sala
                                    dados['q1'+dia_for+'_8cor'] = colors[i]
                                elif frequencia == 'quinzenal II':
                                    dados['q2'+dia_for+'_8'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_8cor'] = colors[i]
                                else:
                                    dados['q1'+dia_for+'_8'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_8'] = turma + ' • ' + sala
                                    dados['q1'+dia_for+'_8cor'] = colors[i]
                                    dados['q2'+dia_for+'_8cor'] = colors[i]

                                if horario_fim == '12:00':
                                    if frequencia == 'quinzenal I':
                                        dados['q1'+dia_for+'_10']= turma + ' • ' + sala
                                        dados['q1'+dia_for+'_10cor'] = colors[i]
                                    elif frequencia == 'quinzenal II':
                                        dados['q2'+dia_for+'_10'] = turma + ' • ' + sala
                                        dados['q2'+dia_for+'_10cor'] = colors[i]
                                    else:
                                        dados['q1'+dia_for+'_10'] = turma + ' • ' + sala
                                        dados['q2'+dia_for+'_10'] = turma + ' • ' + sala
                                        dados['q1'+dia_for+'_10cor'] = colors[i]
                                        dados['q2'+dia_for+'_10cor'] = colors[i]
                                    
                            elif horario == "10:00":
                                if frequencia == 'quinzenal I':
                                    dados['q1'+dia_for+'_10']= turma + ' • ' + sala
                                    dados['q1'+dia_for+'_10cor'] = colors[i]
                                elif frequencia == 'quinzenal II':
                                    dados['q2'+dia_for+'_10'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_10cor'] = colors[i]
                                else:
                                    dados['q1'+dia_for+'_10'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_10'] = turma + ' • ' + sala
                                    dados['q1'+dia_for+'_10cor'] = colors[i]
                                    dados['q2'+dia_for+'_10cor'] = colors[i]

                            elif horario == "14:00":
                                if frequencia == 'quinzenal I':
                                    dados['q1'+dia_for+'_14']= turma + ' • ' + sala
                                    dados['q1'+dia_for+'_14cor'] = colors[i]
                                elif frequencia == 'quinzenal II':
                                    dados['q2'+dia_for+'_14'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_14cor'] = colors[i]
                                else:
                                    dados['q1'+dia_for+'_14'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_14'] = turma + ' • ' + sala
                                    dados['q1'+dia_for+'_14cor'] = colors[i]
                                    dados['q2'+dia_for+'_14cor'] = colors[i]

                                if horario_fim == '18:00':
                                    if frequencia == 'quinzenal I':
                                        dados['q1'+dia_for+'_16']= turma + ' • ' + sala
                                        dados['q1'+dia_for+'_16cor'] = colors[i]
                                    elif frequencia == 'quinzenal II':
                                        dados['q2'+dia_for+'_16'] = turma + ' • ' + sala
                                        dados['q2'+dia_for+'_16cor'] = colors[i]
                                    else:
                                        dados['q1'+dia_for+'_16'] = turma + ' • ' + sala
                                        dados['q2'+dia_for+'_16'] = turma + ' • ' + sala
                                        dados['q1'+dia_for+'_16cor'] = colors[i]
                                        dados['q2'+dia_for+'_16cor'] = colors[i]

                            elif horario == "16:00":
                                if frequencia == 'quinzenal I':
                                    dados['q1'+dia_for+'_16']= turma + ' • ' + sala
                                    dados['q1'+dia_for+'_16cor'] = colors[i]
                                elif frequencia == 'quinzenal II':
                                    dados['q2'+dia_for+'_16'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_16cor'] = colors[i]
                                else:
                                    dados['q1'+dia_for+'_16'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_16'] = turma + ' • ' + sala
                                    dados['q1'+dia_for+'_16cor'] = colors[i]
                                    dados['q2'+dia_for+'_16cor'] = colors[i]
                            
                            elif horario == "17:00":
                                if frequencia == 'quinzenal I':
                                    dados['q1'+dia_for+'_18']= 'Começa as 17 ' + turma + ' • ' + sala 
                                    dados['q1'+dia_for+'_18cor'] = colors[i] 
                                elif frequencia == 'quinzenal II':
                                    dados['q2'+dia_for+'_18'] = 'Começa as 17 ' +turma + ' • ' + sala
                                    dados['q2'+dia_for+'_18cor'] = colors[i] 
                                else:
                                    dados['q1'+dia_for+'_18'] = 'Começa as 17 ' +turma + ' • ' + sala
                                    dados['q2'+dia_for+'_18'] = 'Começa as 17 ' +turma + ' • ' + sala
                                    dados['q1'+dia_for+'_18cor'] = colors[i]
                                    dados['q2'+dia_for+'_18cor'] = colors[i] 

                            elif horario == "19:00":
                                if frequencia == 'quinzenal I':
                                    dados['q1'+dia_for+'_19']= turma + ' • ' + sala
                                    dados['q1'+dia_for+'_19cor'] = colors[i]
                                elif frequencia == 'quinzenal II':
                                    dados['q2'+dia_for+'_19'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_19cor'] = colors[i]
                                else:
                                    dados['q1'+dia_for+'_19'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_19'] = turma + ' • ' + sala
                                    dados['q1'+dia_for+'_19cor'] = colors[i]
                                    dados['q2'+dia_for+'_19cor'] = colors[i]
                                if horario_fim == '23:00':
                                    if frequencia == 'quinzenal I':
                                        dados['q1'+dia_for+'_21']= turma + ' • ' + sala
                                        dados['q1'+dia_for+'_21cor'] = colors[i]
                                    elif frequencia == 'quinzenal II':
                                        dados['q2'+dia_for+'_21'] = turma + ' • ' + sala
                                        dados['q2'+dia_for+'_21cor'] = colors[i]
                                    else:
                                        dados['q1'+dia_for+'_21'] = turma + ' • ' + sala
                                        dados['q2'+dia_for+'_21'] = turma + ' • ' + sala
                                        dados['q1'+dia_for+'_21cor'] = colors[i]
                                        dados['q2'+dia_for+'_21cor'] = colors[i]

                            elif horario == "18:00":
                                if frequencia == 'quinzenal I':
                                    dados['q1'+dia_for+'_18']= turma + ' • ' + sala
                                    dados['q1'+dia_for+'_18cor'] = colors[i]
                                elif frequencia == 'quinzenal II':
                                    dados['q2'+dia_for+'_18'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_18cor'] = colors[i]
                                else:
                                    dados['q1'+dia_for+'_18'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_18'] = turma + ' • ' + sala
                                    dados['q1'+dia_for+'_18cor'] = colors[i]
                                    dados['q2'+dia_for+'_18cor'] = colors[i]
                                if horario_fim == '21:00':
                                    if frequencia == 'quinzenal I':
                                        dados['q1'+dia_for+'_19']= turma + ' • ' + sala
                                        dados['q1'+dia_for+'_19cor'] = colors[i]
                                    elif frequencia == 'quinzenal II':
                                        dados['q2'+dia_for+'_19'] = turma + ' • ' + sala
                                        dados['q2'+dia_for+'_19cor'] = colors[i]
                                    else:
                                        dados['q1'+dia_for+'_19'] = turma + ' • ' + sala
                                        dados['q2'+dia_for+'_19'] = turma + ' • ' + sala
                                        dados['q1'+dia_for+'_19cor'] = colors[i]
                                        dados['q2'+dia_for+'_19cor'] = colors[i]

                            elif horario == "21:00":
                                if frequencia == 'quinzenal I':
                                    dados['q1'+dia_for+'_21']= turma + ' • ' + sala
                                    dados['q1'+dia_for+'_21cor'] = colors[i]
                                elif frequencia == 'quinzenal II':
                                    dados['q2'+dia_for+'_21'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_21cor'] = colors[i]
                                else:
                                    dados['q1'+dia_for+'_21'] = turma + ' • ' + sala
                                    dados['q2'+dia_for+'_21'] = turma + ' • ' + sala
                                    dados['q1'+dia_for+'_21cor'] = colors[i]
                                    dados['q2'+dia_for+'_21cor'] = colors[i]
                
            i+=1

    return render(request, 'calendario/index.html',dados)

def cardapio(request):
    data = Cardapio.objects.get()  # recupere o objeto OCR do banco de dados
    context = {'dados': data}  # coloque o objeto em um dicionário para passar para o contexto
        
    return render(request, 'calendario/cardapio.html', context)
