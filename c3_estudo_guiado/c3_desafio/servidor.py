import socket

from moduloCriptografia import descriptar, encriptar

nome = input('Digite seu nome: ')
print('Aguardando conexão do cliente...')

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8000))
servidor.listen()
cliente, endereco = servidor.accept()

print('Conexão estabelecida: aguardando mensagens...')
print('Após iniciar o chat, digite "Sair" para finalizá-lo!')
print('----------------------------------------------------')

chat = True
while chat:
    mensagem_recebida = descriptar(cliente.recv(2024))
    if mensagem_recebida == 'Sair':
        chat = False
    else:
        print(mensagem_recebida)
        mensagem = input(f'{nome}: ')
        if mensagem == 'Sair':
            cliente.send(encriptar(mensagem))
            chat = False
        else:
            mensagem_para_envio = f'{nome}: {mensagem}'
            cliente.send(encriptar(mensagem_para_envio))

cliente.close()
servidor.close()
