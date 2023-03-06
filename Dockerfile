# Imagem base do Python
FROM python:3.10

WORKDIR /app

# Copiar arquivos necessários para a imagem
COPY requirements.txt .
COPY . .

# Instalar as dependências do Python
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

# Expor a porta em que a aplicação será executada
EXPOSE 8000

# Executar o servidor do Django
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
