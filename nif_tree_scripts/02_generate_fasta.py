import pandas as pd

# Lista de genomas
genomes = [
    "g_Dulcicalothrix_sp", "g_Fortiea_sp", "g_Rivularia_sp_i", "g_Rivularia_sp_ii",
    "s_336_3_sp", "s_Aulosira_anomala_i", "s_Aulosira_anomala_ii", "s_Aulosira_anomala_iii",
    "s_Aulosira_anomala_iv", "s_Calothrix_rhizosoleniae", "s_Dulcicalothrix_desertica",
    "s_NIES_3974", "s_Nostoc_muscorum", "s_PCC_6303", "s_Richelia_intracellularis",
    "s_Rivularia_radiosa"
]

# Itera pelos genomas e cria arquivos fasta
for genome in genomes:
    input_file = f"{genome}.tsv"  # Nome do arquivo gerado anteriormente para cada genoma
    
    try:
        # Carrega o arquivo filtrado do genoma
        df = pd.read_csv(input_file, sep="\t")
        
        # Verifica se as colunas necessárias existem
        if 'aa_sequence' not in df.columns or 'KOfam' not in df.columns:
            print(f"Colunas necessárias não encontradas em {input_file}. Pulando...")
            continue

        # Nome do arquivo fasta de saída
        output_fasta = f"{genome}.fasta"
        
        # Cria o arquivo fasta
        with open(output_fasta, "w") as fasta_file:
            for _, row in df.iterrows():
                gene_name = row['KOfam']
                sequence = row['aa_sequence']
                
                # Escreve o formato fasta
                fasta_file.write(f">{gene_name}\n{sequence}\n")
        
        print(f"Arquivo FASTA criado: {output_fasta}")
    
    except FileNotFoundError:
        print(f"Arquivo {input_file} não encontrado. Pulando...")
