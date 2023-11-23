import datetime
import os
import pysftp
import random

counter = 0

def criar_mensagem():
    # Obtém a data e hora atual
    agora = datetime.datetime.now()
    data_hora = agora.strftime("%Y-%m-%d %H:%M:%S")

    # Solicita ao usuário uma mensagem
    title = input("message title: ")
    mensagem = input("Digite a mensagem que deseja enviar: ")

    # Formata a mensagem
    mensagem_formatada = f"{data_hora},{mensagem}"

    return mensagem_formatada, title

def escrever_log_local(mensagem):
    with open("data.tmp", "w") as arquivo:  # Modo "a" para adicionar ao arquivo
        arquivo.write(mensagem + "\n")

def enviar_para_telemovel(mensagem, title):
    # Configurações SFTP
    endereco_sftp = "192.168.1.10"
    usuario_sftp = "ftpuser"
    senha_sftp = "xpto"

    # Nome do arquivo no telemóvel (data e hora sem espaços)
    rnd = random.randint(0, 10000000000)
    nome_arquivo = title + f"{rnd}"

    # Escreve o arquivo temporário no telemóvel via SFTP
    with pysftp.Connection(endereco_sftp, username=usuario_sftp, password=senha_sftp) as sftp:
        
        sftp.put("data.tmp", nome_arquivo)

print("\x1bc\x1b[43;30mstart application:")

# Chama a função para criar e enviar a mensagem imediatamente
mensagem, title = criar_mensagem()
escrever_log_local(mensagem)
enviar_para_telemovel(mensagem, title)

