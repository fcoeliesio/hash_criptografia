#!/bin/bash

# Solicitar a senha para descriptografar
read -sp "Digite a senha para descriptografar: "  senha
echo

openssl enc -aes-256-cbc -pass pass:"$senha" -d -in mensagem.enc -out mensagem.dec

echo "Mensagem descriptografada com sucesso!"
