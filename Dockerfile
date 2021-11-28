#DEFINE A IMAGEM BASE
FROM python:3.9

# VARIAVEL DE AMBIENTE PARA OS ARQUIVOS .PYC
ENV PYTHONDONTWRITEBYTECODE 1
#VARIAVEL DE AMBIENTE PARA OS ARQUIVOS NAO ARMAZENA OS LOG
ENV PYTHONUNBUFFERED 1
#PEGA MEU ARQUIVO REQUERIMENTE PARA O WORKDIR
WORKDIR /code
#COPIA O ARQUIVO
COPY requirements.txt .
#RODAS O PIP INSTALL 
RUN pip install -r requirements.txt
#COPIA TUDO DA PASTA LOCAL PARA A PASTA CODE 
COPY . .