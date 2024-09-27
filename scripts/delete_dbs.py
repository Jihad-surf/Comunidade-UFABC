from calendarioapp.models import TurmaPorRA
from calendarioapp.models import Salas

def run():
    TurmaPorRA.objects.all().delete()
    Salas.objects.all().delete()
    #deleta tudo
    
