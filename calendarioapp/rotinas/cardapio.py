from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from calendarioapp.models import Cardapio
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


def cardapio():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)

    navegador.get("https://proap.ufabc.edu.br/nutricao-e-restaurantes-universitarios/cardapio-semanal")
    time.sleep(2)
    #segunda
    seg_principal_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[2]/td[1]/ul[1]/li[1]').text
    seg_veg_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[2]/td[1]/ul[1]/li[2]').text
    seg_guarnicao_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[2]/td[1]/ul[1]/li[2]').text
    
    seg_principal_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[2]/td[1]/ul[2]/li[1]').text
    seg_veg_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[2]/td[1]/ul[2]/li[2]').text
    seg_guarnicao_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[2]/td[1]/ul[2]/li[2]').text
    
    seg_saladas = navegador.find_element('xpath',
                                         '//*[@id="content-section"]/div[1]/div/table/tbody/tr[2]/td[1]/ul[3]/li').text
    seg_sobremesa = navegador.find_element('xpath',
                                         '//*[@id="content-section"]/div[1]/div/table/tbody/tr[2]/td[1]/ul[4]/li').text
    
    #terca
    ter_principal_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[4]/td[1]/ul[1]/li[1]').text
    ter_veg_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[4]/td[1]/ul[1]/li[2]').text
    ter_guarnicao_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[4]/td[1]/ul[1]/li[2]').text
    
    ter_principal_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[4]/td[1]/ul[2]/li[1]').text
    ter_veg_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[4]/td[1]/ul[2]/li[2]').text
    ter_guarnicao_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[4]/td[1]/ul[2]/li[2]').text
    
    ter_saladas = navegador.find_element('xpath',
                                         '//*[@id="content-section"]/div[1]/div/table/tbody/tr[4]/td[1]/ul[3]/li').text
    ter_sobremesa = navegador.find_element('xpath',
                                         '//*[@id="content-section"]/div[1]/div/table/tbody/tr[4]/td[1]/ul[4]/li').text
    
    #quarta
    quar_principal_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[6]/td[1]/ul[1]/li[1]').text
    quar_veg_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[6]/td[1]/ul[1]/li[2]').text
    quar_guarnicao_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[6]/td[1]/ul[1]/li[2]').text
    
    quar_principal_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[6]/td[1]/ul[2]/li[1]').text
    quar_veg_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[6]/td[1]/ul[2]/li[2]').text
    quar_guarnicao_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[6]/td[1]/ul[2]/li[2]').text
    
    quar_saladas = navegador.find_element('xpath',
                                         '//*[@id="content-section"]/div[1]/div/table/tbody/tr[6]/td[1]/ul[3]/li').text
    quar_sobremesa = navegador.find_element('xpath',
                                         '//*[@id="content-section"]/div[1]/div/table/tbody/tr[6]/td[1]/ul[4]/li').text
    
    #quinta
    quinta_principal_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[8]/td[1]/ul[1]/li[1]').text
    quinta_veg_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[8]/td[1]/ul[1]/li[2]').text
    quinta_guarnicao_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[8]/td[1]/ul[1]/li[2]').text
    
    quinta_principal_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[8]/td[1]/ul[2]/li[1]').text
    quinta_veg_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[8]/td[1]/ul[2]/li[2]').text
    quinta_guarnicao_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[8]/td[1]/ul[2]/li[2]').text
    
    quinta_saladas = navegador.find_element('xpath',
                                         '//*[@id="content-section"]/div[1]/div/table/tbody/tr[8]/td[1]/ul[3]/li').text
    quinta_sobremesa = navegador.find_element('xpath',
                                         '//*[@id="content-section"]/div[1]/div/table/tbody/tr[8]/td[1]/ul[4]/li').text
    
    #sexta
    sexta_principal_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[10]/td[1]/ul[1]/li[1]').text
    sexta_veg_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[10]/td[1]/ul[1]/li[2]').text
    sexta_guarnicao_a = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[10]/td[1]/ul[1]/li[2]').text
    
    sexta_principal_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[10]/td[1]/ul[2]/li[1]').text
    sexta_veg_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[10]/td[1]/ul[2]/li[2]').text
    sexta_guarnicao_j = navegador.find_element('xpath',
                           '//*[@id="content-section"]/div[1]/div/table/tbody/tr[10]/td[1]/ul[2]/li[2]').text
    
    sexta_saladas = navegador.find_element('xpath',
                                         '//*[@id="content-section"]/div[1]/div/table/tbody/tr[10]/td[1]/ul[3]/li').text
    sexta_sobremesa = navegador.find_element('xpath',
                                         '//*[@id="content-section"]/div[1]/div/table/tbody/tr[10]/td[1]/ul[4]/li').text
    
    seg_dia =navegador.find_element('xpath',
                                    '//*[@id="content-section"]/div[1]/div/table/tbody/tr[1]/td[1]/h2').text
    ter_dia =  navegador.find_element('xpath',
                                      '//*[@id="content-section"]/div[1]/div/table/tbody/tr[3]/td[1]/h2').text
    quar_dia = navegador.find_element('xpath',
                                      '//*[@id="content-section"]/div[1]/div/table/tbody/tr[5]/td[1]/h2').text
    quinta_dia = navegador.find_element('xpath',
                                      '//*[@id="content-section"]/div[1]/div/table/tbody/tr[7]/td[1]/h2').text
    sexta_dia = navegador.find_element('xpath',
                                      '//*[@id="content-section"]/div[1]/div/table/tbody/tr[9]/td[1]/h2').text

    Cardapio.objects.all().delete()
    Cardapio.objects.create(
        #seg
        seg_principal_a=seg_principal_a.split(':')[1],
        seg_veg_a=seg_veg_a.split(':')[1],
        seg_guarnicao_a=seg_guarnicao_a.split(':')[1],

        seg_principal_j=seg_principal_j.split(':')[1],
        seg_veg_j=seg_veg_j.split(':')[1],
        seg_guarnicao_j=seg_guarnicao_j.split(':')[1],

        seg_saladas=seg_saladas,
        seg_sobremesa=seg_sobremesa,

        #terca
        ter_principal_a=ter_principal_a.split(':')[1],
        ter_veg_a=ter_veg_a.split(':')[1],
        ter_guarnicao_a=ter_guarnicao_a.split(':')[1],

        ter_principal_j=ter_principal_j.split(':')[1],
        ter_veg_j=ter_veg_j.split(':')[1],
        ter_guarnicao_j=ter_guarnicao_j.split(':')[1],

        ter_saladas=ter_saladas,
        ter_sobremesa=ter_sobremesa,

        #quarta
        quar_principal_a=quar_principal_a.split(':')[1],
        quar_veg_a=quar_veg_a.split(':')[1],
        quar_guarnicao_a=quar_guarnicao_a.split(':')[1],

        quar_principal_j=quar_principal_j.split(':')[1],
        quar_veg_j=quar_veg_j.split(':')[1],
        quar_guarnicao_j=quar_guarnicao_j.split(':')[1],

        quar_saladas=quar_saladas,
        quar_sobremesa=quar_sobremesa,

        #quinta
        quinta_principal_a=quinta_principal_a.split(':')[1],
        quinta_veg_a=quinta_veg_a.split(':')[1],
        quinta_guarnicao_a=quinta_guarnicao_a.split(':')[1],

        quinta_principal_j=quinta_principal_j.split(':')[1],
        quinta_veg_j=quinta_veg_j.split(':')[1],
        quinta_guarnicao_j=quinta_guarnicao_j.split(':')[1],

        quinta_saladas=quinta_saladas,
        quinta_sobremesa=quinta_sobremesa,

        #sexta
        sexta_principal_a=sexta_principal_a.split(':')[1],
        sexta_veg_a=sexta_veg_a.split(':')[1],
        sexta_guarnicao_a=sexta_guarnicao_a.split(':')[1],

        sexta_principal_j=sexta_principal_j.split(':')[1],
        sexta_veg_j=sexta_veg_j.split(':')[1],
        sexta_guarnicao_j=sexta_guarnicao_j.split(':')[1],

        sexta_saladas=sexta_saladas,
        sexta_sobremesa=sexta_sobremesa,

        seg_dia=seg_dia,
        ter_dia=ter_dia,
        quar_dia=quar_dia,
        quinta_dia=quinta_dia,
        sexta_dia=sexta_dia
    )
    print('hello 15 min')

def start_cardapio():
    scheduler = BackgroundScheduler()

    scheduler.add_job(cardapio, 'date')
    scheduler.add_job(cardapio, 'cron', day_of_week='mon', hour='8-11')
    # Iniciando o agendador
    scheduler.start()

"""
trigger_2 = IntervalTrigger(seconds=5)
scheduler.add_job(teste, trigger=trigger_2, timezone="America/Sao_Paulo")
scheduler.start()
"""   