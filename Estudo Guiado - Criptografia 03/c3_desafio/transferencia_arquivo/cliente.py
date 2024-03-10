import socket
from cryptography.fernet import Fernet
import os

def carregar_chave():
    if os.path.exists('chave.txt'):
        with open('chave.txt', 'rb') as arquivo_chave:
            chave = arquivo_chave.read()
    else:
        chave = Fernet.generate_key()
        with open('chave.txt', 'wb') as arquivo_chave:
            arquivo_chave.write(chave)
    return chave

chave = carregar_chave()
cipher = Fernet(chave)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8000))

# Lendo o arquivo e enviando em partes
with open('brio.jpg', 'rb') as arquivo:
    dados = arquivo.read()
    dados_cifrados = cipher.encrypt(dados)
    cliente.sendall(dados_cifrados)

print('Arquivo enviado com sucesso!')

cliente.close()
