# Passo 2: Importação do Módulo e Geração da Chave de Criptografia
from cryptography.fernet import Fernet

# Geração da chave de criptografia
chave = Fernet.generate_key()
cipher_suite = Fernet(chave)

# Passo 3: Cifragem do Arquivo de Texto
with open('arquivo.txt', 'rb') as arquivo:
    texto = arquivo.read()
    texto_cifrado = cipher_suite.encrypt(texto)

# Salva o texto cifrado em um novo arquivo
with open('arquivo_cifrado.txt', 'wb') as arquivo_cifrado:
    arquivo_cifrado.write(texto_cifrado)

# Passo 4: Decigradem do Arquivo Cifrado
with open('arquivo_cifrado.txt', 'rb') as arquivo_cifrado:
    texto_cifrado = arquivo_cifrado.read()
    texto_decifrado = cipher_suite.decrypt(texto_cifrado)

# Salva o texto decifrado em um novo arquivo
with open('arquivo_decifrado.txt', 'wb') as arquivo_decifrado:
    arquivo_decifrado.write(texto_decifrado)
