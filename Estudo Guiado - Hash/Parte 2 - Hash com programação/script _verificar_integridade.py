import hashlib, timeit

def calcular_hash(arquivo):
    sha512 = hashlib.sha512()
    with open(arquivo, 'rb') as f:
        # leitura do arquivo em blocos para eficiência
        for bloco in iter(lambda: f.read(4096), b''):
            sha512.update(bloco)
    return sha512.hexdigest()

def salvar_hash(arquivo, hash_calculado):
    with open(arquivo + '_hash.txt', 'w') as f:
        f.write(hash_calculado)

def verificar_integridade(arquivo, hash_salvo):
    hash_calculado = calcular_hash(arquivo)
    print(f'Hash calculado:\t {hash_calculado}')
    print(f'Hash arquivo:\t {hash_salvo}')
    return hash_calculado == hash_salvo

def main():
    arquivo_original = 'exemplo.txt'

    # Verificação de Integridade
    hash_salvo = open(arquivo_original + "_hash.txt").read()
    if verificar_integridade(arquivo_original, hash_salvo):
        print('A integridade do arquivo foi preservada.')
    else:
        print('Atenção! O arquivo foi modificado!')

tempo = timeit.timeit(main, number=1)
print(f'Tempo: {tempo}')



