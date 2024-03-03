#!/bin/bash

echo "---------"
echo "Mensagem original: $(cat mensagem.txt)"
echo "----------"

echo "Clovis de Barros Filho" >> mensagem.txt
echo "Mensagem modificada:"
cat mensagem.txt
echo "---------"

# Verificação de integridade
echo "Verificação de integridade do Hash:"
sha256sum -c hash_original.txt
