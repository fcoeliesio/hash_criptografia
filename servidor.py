import socket
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
import time

# Criação da chave e armazenamento dela em um arquivo .TXT
chave_aes = get_random_bytes(16)
chave_hmac = get_random_bytes(16)

with open("chave.txt", "wb") as arquivo_chave:
    arquivo_chave.write(chave_aes + chave_hmac)

cipher = AES.new(chave_aes, AES.MODE_CTR)

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

hmac = HMAC.new(chave_hmac, digestmod=SHA256)
tag = hmac.update(cipher.nonce + dados_recebidos).digest()

# Salvando arquivo antes de descriptografá-lo
with open("brio_criptografado.jpg", "wb") as arquivo:
    arquivo.write(tag)
    arquivo.write(cipher.nonce)
    arquivo.write(dados_recebidos)

# Medição do tempo de criptografia
inicio_criptografia = time.time()
with open("brio_criptografado.jpg", "rb") as f:
    # Lê a tag HMAC, nonce e o texto cifrado do arquivo
    tag = f.read(32)
    nonce = f.read(8)
    dados_recebidos = f.read()
fim_criptografia = time.time()
tempo_criptografia = fim_criptografia - inicio_criptografia
print("Tempo para criptografar:", tempo_criptografia, "segundos")

# Inicializa o objeto HMAC com hmac_key e a função de hash SHA256
hmac = HMAC.new(chave_hmac, digestmod=SHA256)
# Atualiza o HMAC com o nonce e o texto cifrado, e então verifica a tag
tag_calc = hmac.update(nonce + dados_recebidos).digest()

if tag == tag_calc:
    print("HMAC verificado com sucesso!")
else:
    print("A mensagem foi modificada!")


with open("brio_recebido.jpg", "wb") as arquivo:
    arquivo.write(cipher.decrypt(dados_recebidos))

print("Servidor: arquivo recebido com sucesso!")

cliente.close()
servidor.close()
