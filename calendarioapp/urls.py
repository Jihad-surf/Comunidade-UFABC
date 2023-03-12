from django.urls import path
from calendarioapp.views import index, cardapio

urlpatterns = [ 
    path('',index, name='home'),
    path('cardapio',cardapio, name='cardapio')
]