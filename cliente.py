import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

chave = get_random_bytes(16)

with open("chave.txt", "wb") as arquivo_chave:
    arquivo_chave.write(chave)

cipher = AES.new(chave, AES.MODE_CCM)

# Iniciando conexão com o servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 8000))

# Enviando os dados cifrados
with open("brio.jpg", "rb") as arquivo:
    dados = arquivo.read()
    dados_cifrados, tag = cipher.encrypt_and_digest(dados)
    cliente.sendall(dados_cifrados)
    cliente.sendall(tag)

print("Cliente: arquivo enviado com sucesso!")

cliente.close()