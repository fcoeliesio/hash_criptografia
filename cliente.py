from cryptography.fernet import Fernet
import socket
from Crypto.Cipher import AES

# Lendo a chave criada no servidor
with open('chave.txt', 'rb') as arquivo_chave:
    chave = arquivo_chave.read()
cipher = AES.new(chave, AES.MODE_OCB)

# Iniciando conexão com o servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8000))

# Enviando o arquivo
with open('brio.jpg', 'rb') as arquivo:
    dados = arquivo.read()
    dados_cifrados = cipher.encrypt(dados)
    cliente.sendall(dados_cifrados)

print('Cliente: arquivo enviado com sucesso!')

cliente.close()