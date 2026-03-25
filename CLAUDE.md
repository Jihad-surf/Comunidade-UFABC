# UFABC Calendario

## Visao Geral

Aplicacao web Django para alunos da UFABC consultarem grade de horarios e cardapio do restaurante universitario. O aluno insere seu RA e visualiza suas materias organizadas em uma grade semanal com suporte a semanas quinzenais (q1/q2).

## Stack

- **Python 3.10** / **Django 4.1**
- **MySQL** (Railway) — credenciais em `configs/settings.py`
- **Gunicorn** + **WhiteNoise** para deploy
- **Dockerfile** e **Procfile** para deploy (Railway)
- **SECRET_KEY** carregada via `.env` com `python-dotenv`

## Estrutura do Projeto

```
configs/          # Projeto Django (settings, urls, wsgi, asgi)
  static/         # Arquivos estaticos (CSS, imagens)
calendarioapp/    # App principal
  models.py       # Count, HorarioAula, TurmaPorRA, Salas, Cardapio
  views.py        # index (grade de horarios), cardapio
  urls.py         # Rotas: / (home), /cardapio
  rotinas/        # Scripts de rotinas (cardapio)
  migrations/     # Migrations Django
scripts/          # Scripts de carga de dados (load_salas, load_raTurma, delete_dbs)
templates/        # Templates HTML (calendario/index.html, calendario/cardapio.html)
staticfiles/      # Arquivos coletados pelo collectstatic
venv/             # Virtualenv local
```

## Comandos

```bash
# Ativar virtualenv
source venv/Scripts/activate   # Windows (Git Bash)

# Rodar servidor local
python manage.py runserver

# Migrations
python manage.py makemigrations
python manage.py migrate

# Coletar arquivos estaticos
python manage.py collectstatic

# Rodar scripts de carga de dados
python manage.py runscript load_salas
python manage.py runscript load_raTurma
python manage.py runscript delete_dbs
```

## Convencoes

- Idioma do projeto: **portugues brasileiro** (LANGUAGE_CODE = pt-br, TIME_ZONE = America/Sao_Paulo)
- Settings module: `configs.settings`
- Templates ficam em `templates/calendario/`
- Arquivos estaticos de desenvolvimento ficam em `configs/static/`
- Scripts de dados usam `django-extensions` (`runscript`)
