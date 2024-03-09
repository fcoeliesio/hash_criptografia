#!/bin/bash

# Solicitar a senha e sua confirmação
read -sp "Digite sua senha: "  senha1
echo
read -sp "Confirme sua senha: " senha2
echo

# Verificar se as senhas correspondem
if [ "$senha1" != "$senha2" ]; then
    echo "As senhas não correspondem."
    exit 1
fi

# Mensagem e seu conteúdo
echo "Quem tem acesso à informação tem medo!" > mensagem.txt

# Criptografando a mensagem usando o algoritmo AES-256-CBC
openssl enc -aes-256-cbc -pass pass:"$senha1" -in mensagem.txt -out mensagem.enc

echo "Mensagem criptografada com sucesso!"
