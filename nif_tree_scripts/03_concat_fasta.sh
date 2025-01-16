#!/bin/bash

# Definir o diretório com os arquivos fasta
input_dir="/home/fluvio/Richelia_project/fasta/"

# Nome do arquivo de saída
output_file="concatenado.fasta"

# Criar ou limpar o arquivo de saída
> "$output_file"

# Loop para concatenar todos os arquivos .fasta no diretório
for fasta_file in "$input_dir"/*.fasta; do
    if [ -f "$fasta_file" ]; then
        cat "$fasta_file" >> "$output_file"
        echo "" >> "$output_file"  # Adicionar uma nova linha para separar os arquivos
    fi
done

echo "Arquivos concatenados em $output_file"
