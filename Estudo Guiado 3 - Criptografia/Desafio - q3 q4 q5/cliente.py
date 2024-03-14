import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

chave = get_random_bytes(16)

cipher = AES.new(chave, AES.MODE_EAX)
nonce = cipher.nonce

# Iniciando conexão com o servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 8000))

# Enviando os dados cifrados
with open("brio.jpg", "rb") as arquivo:
    dados = arquivo.read()
    dados_cifrados = cipher.encrypt(dados)

# Adiciona a chave e o cipher.nonce ao arquivo encriptado
with open("encrypted_cliente.bin", "wb") as f:
    f.write(chave)
    f.write(nonce)
    f.write(dados_cifrados)

# Envio do arquivo encriptado para o destino
with open("encrypted_cliente.bin", "rb") as f:
    envio = f.read()
    cliente.sendall(envio)

print("Cliente: arquivo enviado com sucesso!")

cliente.close()