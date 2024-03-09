#!/bin/bash

echo "---------"
echo "Mensagem original: $(cat mensagem.txt)"
echo "----------"

echo '"Minha cabeça é grande como os meus poemas."' >mensagem.txt
echo "                 Carlos Drummond de Andrade" >>mensagem.txt
echo "Mensagem modificada:"
cat mensagem.txt
echo "---------"

# Verificação de integridade
echo "Verificação de integridade do Hash:"
sha256sum -c hash_original.txt
