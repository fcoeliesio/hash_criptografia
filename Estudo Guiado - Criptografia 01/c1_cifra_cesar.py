def cifra_cesar(texto, deslocamento):
    texto_substituido = ''
    for letra in texto:
        texto_substituido += chr(ord(letra) + deslocamento)
    return texto_substituido

texto = input('Digite o texto que deseja criptografar: ')
deslocamento = int(input('Digite a distância que deseja usar: '))

print(f'Resultado: {cifra_cesar(texto, deslocamento)}')
