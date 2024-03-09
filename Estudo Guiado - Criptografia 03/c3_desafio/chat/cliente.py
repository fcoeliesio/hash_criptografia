import socket
from moduloCriptografia import descriptar, encriptar

nome = input('Digite seu nome: ')

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost',8000))

print('Conexão com o servidor estabelecida!')
print('Digite "Sair" para finalizar o chat!')
print('------------------------------------')

chat = True
while chat:
    mensagem = input(f'{nome}: ')
    if mensagem.upper() == 'SAIR':
        cliente.send(encriptar(mensagem))
        chat = False
    else:
        mensagem_para_envio = f'{nome}: {mensagem}'
        cliente.send(encriptar(mensagem_para_envio))
        mensagem_recebida = descriptar(cliente.recv(2024))
        if mensagem_recebida.upper() == 'SAIR':
            chat = False
        else:
            print(mensagem_recebida)

cliente.close()
