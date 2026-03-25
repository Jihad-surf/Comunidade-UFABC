# Imagem base do Python
FROM python:3.10

WORKDIR /app

# Copiar arquivos necessários para a imagem
COPY requirements.txt .
COPY . .

# Instalar as dependências do Python
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

# Executar com gunicorn na porta definida pelo Railway ($PORT)
CMD gunicorn configs.wsgi --bind 0.0.0.0:$PORT
