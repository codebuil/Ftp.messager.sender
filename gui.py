import datetime
import os
from ftplib import FTP
import tkinter as tk

def enviar_mensagem():
    # Obtém o conteúdo da área de texto
    mensagem = texto_area.get("1.0", "end-1c")

    # Obtém a data e hora atual
    agora = datetime.datetime.now()
    data_hora = agora.strftime("%Y-%m-%d %H:%M:%S")

    # Formata a mensagem
    mensagem_formatada = f"{data_hora},{mensagem}"

    # Escreve a mensagem localmente
    escrever_log_local(mensagem_formatada)

    # Envia a mensagem para o telemóvel via FTP
    enviar_para_telemovel(mensagem_formatada)

def escrever_log_local(mensagem):
    with open("data.tmp", "w") as arquivo:
        arquivo.write(mensagem + "\n")

def enviar_para_telemovel(mensagem):
    # Configurações FTP
    endereco_ftp = "192.168.1.5"
    porta_ftp = 2121

    # Conecta ao servidor FTP
    with FTP() as ftp:
        ftp.connect(endereco_ftp, porta_ftp)
        ftp.login()

        # Nome do arquivo no telemóvel (data e hora sem espaços)
        nome_arquivo = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.txt")

         # Escreve o arquivo temporário no telemóvel
        with open("data.tmp", "rb") as arquivo:
            ftp.storbinary(f"STOR {nome_arquivo}", arquivo)



# Configuração da interface gráfica
root = tk.Tk()
root.title("Enviador de Mensagens")
root.configure(bg="brown", width=800, height=600)  # Define a cor de 

# Área de texto
texto_area = tk.Text(root, height=5, width=50)
texto_area.pack(padx=10, pady=10)

# Botão de envio
botao_enviar = tk.Button(root, text="Enviar Mensagem", command=enviar_mensagem)
botao_enviar.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()

