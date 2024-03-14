import socket
from Crypto.Cipher import AES

print("Aguardando arquivo do cliente...")

# Iniciando o servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 8000))
servidor.listen()

cliente, endereco = servidor.accept()

# Lendo a chave do arquivo
with open("chave.txt", "rb") as arquivo_chave:
    chave = arquivo_chave.read()

# Recebendo os dados em partes
dados_recebidos = b""
while True:
    parte = cliente.recv(1024)
    if not parte:
        break
    dados_recebidos += parte

# Criando o objeto cipher após receber os dados
cipher = AES.new(chave, AES.MODE_CCM)

with open("brio_cifrado.jpg", "wb") as arquivo:
    arquivo.write(dados_recebidos)

try:
    # Decifrando os dados e verificando a autenticidade
    dados_decifrados = cipher.decrypt(dados_recebidos)
    with open("brio_decifrado.jpg", "wb") as arquivo:
        arquivo.write(dados_decifrados)
except (ValueError, KeyError):
    print("Incorrect decryption")

print("Servidor: arquivo recebido com sucesso!")

cliente.close()
servidor.close()