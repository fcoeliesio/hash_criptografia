import socket
from chave import cipher

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8000))

# Lendo o arquivo e enviando em partes
with open('brio.jpg', 'rb') as arquivo:
    dados = arquivo.read()
    dados_cifrados = cipher.encrypt(dados)
    cliente.sendall(dados_cifrados)

print('Arquivo enviado com sucesso!')

cliente.close()
