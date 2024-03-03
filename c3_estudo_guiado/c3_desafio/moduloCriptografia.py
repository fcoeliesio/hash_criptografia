from cryptography.fernet import Fernet

def carregar_chave():
    with open("chave.txt", "rb") as arquivo_chave:
        chave = arquivo_chave.read()
    return chave

chave = carregar_chave()
cipher = Fernet(chave)

def encriptar(mensagem):
    return cipher.encrypt(mensagem.encode('utf-8'))

def descriptar(mensagem):
    return cipher.decrypt(mensagem).decode('utf-8')
