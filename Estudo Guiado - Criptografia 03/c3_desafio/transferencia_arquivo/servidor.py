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

print('Aguardando arquivo do cliente...')

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8000))
servidor.listen()

cliente, endereco = servidor.accept()

# Recebendo os dados em partes
dados_recebidos = b''
while True:
    parte = cliente.recv(1024)
    if not parte:
        break
    dados_recebidos += parte

# Salvando arquivo antes de descriptografá-lo
with open('tenho_brio_criptografado.jpg', 'wb') as arquivo:
    arquivo.write(dados_recebidos)

# Descriptografando os dados recebidos
dados_decifrados = cipher.decrypt(dados_recebidos)

# Salvando os dados recebidos em um arquivo
with open('tenho_brio.jpg', 'wb') as arquivo:
    arquivo.write(dados_decifrados)

print('Arquivo recebido!')

cliente.close()
servidor.close()
