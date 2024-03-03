import hashlib

def calcular_hash(arquivo):
    sha256 = hashlib.sha256()
    with open(arquivo, 'rb') as f:
        # leitura do arquivo em blocos para eficiência
        for bloco in iter(lambda: f.read(4096), b''):
            sha256.update(bloco)
    return sha256.hexdigest()

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
    hash_calculado = calcular_hash(arquivo_original)
    salvar_hash(arquivo_original, hash_calculado)
    print('Hash salvo em arquivo!')

if __name__ == "__main__":
    main()

