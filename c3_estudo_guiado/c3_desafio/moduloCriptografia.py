from cryptography.fernet import Fernet

def carregar_chave():
    with open("chave.txt", "rb") as arquivo_chave:
        chave = arquivo_chave.read()
    return chave

chave = carregar_chave()
cipher = Fernet(chave)

def encriptar(mensagem_enviada):
    return cipher.encrypt(mensagem_enviada.encode('utf-8'))

def descriptar(mensagem_recebida):
    return cipher.decrypt(mensagem_recebida).decode('utf-8')
