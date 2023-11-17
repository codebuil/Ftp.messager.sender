import datetime
import os
from ftplib import FTP
import random
counter=0
def criar_mensagem():
    # Obtém a data e hora atual
    agora = datetime.datetime.now()
    data_hora = agora.strftime("%Y-%m-%d %H:%M:%S")

    # Solicita ao usuário uma mensagem
    title= input("message title: ")
    mensagem = input("Digite a mensagem que deseja enviar: ")
    
    # Formata a mensagem
    mensagem_formatada = f"{data_hora},{mensagem}"

    return mensagem_formatada,title

def escrever_log_local(mensagem):
    with open("data.tmp", "w") as arquivo:
        arquivo.write(mensagem + "\n")

def enviar_para_telemovel(mensagem,title):
    # Configurações FTP
    endereco_ftp = "192.168.1.6"
    porta_ftp = 2121

    # Conecta ao servidor FTP
    with FTP() as ftp:
        ftp.connect(endereco_ftp, porta_ftp)
        ftp.login()

        # Nome do arquivo no telemóvel (data e hora sem espaços)
        rnd=random.randint(0,10000000000 )
        nome_arquivo = title+f"{rnd}"


        # Escreve o arquivo temporário no telemóvel
        with open("data.tmp", "rb") as arquivo:
            ftp.storbinary(f"STOR {nome_arquivo}", arquivo)


print("\x1bc\x1b[43;30mstart application:")

# Chama a função para criar e enviar a mensagem imediatamente
title,mensagem = criar_mensagem()
escrever_log_local(mensagem)
enviar_para_telemovel(mensagem,title)


