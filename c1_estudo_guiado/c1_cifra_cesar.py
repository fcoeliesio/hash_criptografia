def cifra_cesar(texto, distancia):
    texto_substituido = ''
    for letra in texto:
        texto_substituido += chr(ord(letra) + distancia)
    return texto_substituido

texto = input('Digite o texto que deseja criptografar: ')
distancia = int(input('Digite a distância que deseja usar: '))

print(f'O texto criptografado é: {cifra_cesar(texto, distancia)}')
