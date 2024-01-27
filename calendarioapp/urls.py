from django.urls import path
from calendarioapp.views import index, cardapio
#from calendarioapp.rotinas.cardapio import start_cardapio

# inicia as rotinas
#start_cardapio()

urlpatterns = [ 
    path('',index, name='home'),
    path('cardapio',cardapio, name='cardapio'),
]