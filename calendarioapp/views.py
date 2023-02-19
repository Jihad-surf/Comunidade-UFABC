from django.shortcuts import render

# Create your views here.
def index(request):
    dados = {
    
    'segunda': {
        "8": {'materia':"Bases matematicas B1 S230-1", 'cor':''},
        "10": {'materia':"", 'cor':''},
        "12": {'materia':"", 'cor':''},
        "14": {'materia':"", 'cor':''},
        "16": {'materia':"", 'cor':''},
        "18": {'materia':"", 'cor':''},
        "19": {'materia':"", 'cor':''},
        "21": {'materia':"Bases matematicas B1 S230-1", 'cor':'black'},
        }, 
    'terca': {
        "8": {'materia':"Bases matematicas B1 S230-1", 'cor':'green'},
        "10": {'materia':"", 'cor':''},
        "12": {'materia':"", 'cor':''},
        "14": {'materia':"", 'cor':''},
        "16": {'materia':"", 'cor':''},
        "18": {'materia':"", 'cor':''},
        "19": {'materia':"", 'cor':''},
        "21": {'materia':"Bases matematicas B1 S230-1", 'cor':'black'},
        },
    'quarta': {
        "8": {'materia':"Bases matematicas B1 S230-1", 'cor':'blue'},
        "10": {'materia':"", 'cor':''},
        "12": {'materia':"", 'cor':''},
        "14": {'materia':"", 'cor':''},
        "16": {'materia':"", 'cor':''},
        "18": {'materia':"", 'cor':''},
        "19": {'materia':"", 'cor':''},
        "21": {'materia':"Bases matematicas B1 S230-1", 'cor':'black'},
        },
    'quinta': {
        "8": {'materia':"Bases matematicas B1 S230-1", 'cor':'blue'},
        "10": {'materia':"", 'cor':''},
        "12": {'materia':"", 'cor':''},
        "14": {'materia':"", 'cor':''},
        "16": {'materia':"", 'cor':''},
        "18": {'materia':"", 'cor':''},
        "19": {'materia':"", 'cor':''},
        "21": {'materia':"Bases matematicas B1 S230-1", 'cor':'black'},
        },
    'sexta': {
        "8": {'materia':"Bases matematicas B1 S230-1", 'cor':'blue'},
        "10": {'materia':"", 'cor':''},
        "12": {'materia':"", 'cor':''},
        "14": {'materia':"", 'cor':''},
        "16": {'materia':"", 'cor':''},
        "18": {'materia':"", 'cor':''},
        "19": {'materia':"", 'cor':''},
        "21": {'materia':"Bases matematicas B1 S230-1", 'cor':'black'},
        }
    }
    return render(request, 'calendario/index.html', dados)

