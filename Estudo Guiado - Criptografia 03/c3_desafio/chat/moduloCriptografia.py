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

def encriptar(mensagem_enviada):
    return cipher.encrypt(mensagem_enviada.encode('utf-8'))

def descriptar(mensagem_recebida):
    return cipher.decrypt(mensagem_recebida).decode('utf-8')
