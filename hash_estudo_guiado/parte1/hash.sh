#!/bin/bash

# Criando uma mensagem
echo "É só uma questão de brio!" > mensagem.txt
echo "Mensagem criada: $(cat mensagem.txt)"

# Geração do Hash para o arquivo original
sha256sum mensagem.txt > hash_original.txt
echo "Hash gerado: $(cat hash_original.txt)"

# Verificação de integridade do hash
echo "Verificaçao de integridade do Hash"
sha256sum -c hash_original.txt
