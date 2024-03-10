import socket
from chave import cipher

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
with open('brio_criptografado.jpg', 'wb') as arquivo:
    arquivo.write(dados_recebidos)

# Descriptografando os dados recebidos
dados_decifrados = cipher.decrypt(dados_recebidos)

# Salvando os dados recebidos em um arquivo
with open('brio_recebido.jpg', 'wb') as arquivo:
    arquivo.write(dados_decifrados)

print('Arquivo recebido!')

cliente.close()
servidor.close()
