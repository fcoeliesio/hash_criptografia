import socket
from Crypto.Cipher import AES

print("Aguardando arquivo do cliente...")

# Iniciando o servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 8000))
servidor.listen()

cliente, endereco = servidor.accept()

# Recebendo os dados em partes
dados_recebidos = b""
while True:
    parte = cliente.recv(1024)
    if not parte:
        break
    dados_recebidos += parte

# Montando o arquivo encriptado recebido
with open("encrypted_server.bin", 'wb') as arquivo_bruto:
    arquivo_bruto.write(dados_recebidos)

# # Lendo a chave do arquivo
with open("encrypted_server.bin", "rb") as arquivo_chave:
    # Recuperação da chave
    chave = arquivo_chave.read(16)
    # Recuperação do cipher.nonce
    nonce = arquivo_chave.read(16)
    # Recuperação do conteúdo encriptado da mensagem
    brio_cifrado = arquivo_chave.read()

# Criando o objeto cipher após receber os dados
cipher = AES.new(chave, AES.MODE_EAX, nonce=nonce)

try:
    # Decifrando os dados e verificando a autenticidade
    dados_decifrados = cipher.decrypt(brio_cifrado)
    with open("image_decifrada.jpg", "wb") as arquivo_decifrado:
        arquivo_decifrado.write(dados_decifrados)
except (ValueError, KeyError):
    print("Incorrect decryption")

print("Servidor: arquivo recebido com sucesso!")

cliente.close()
servidor.close()