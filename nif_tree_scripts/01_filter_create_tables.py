import pandas as pd

# Etapa 1: Filtro inicial
input_file = "Rivu_pan_gene_clusters_summary.txt"
core_output_file = "filtered_core.tsv"

# Carrega o arquivo original
df = pd.read_csv(input_file, sep="\t")

# Filtra linhas onde a coluna 'bin_name' contém 'Core_genome'
filtered_df = df[df['bin_name'] == 'Core_genome']

# Salva o filtro inicial
filtered_df.to_csv(core_output_file, sep="\t", index=False)
print(f"Arquivo filtrado salvo como: {core_output_file}")

# Etapa 2: Filtro para proteínas de fixação de nitrogênio
nitrogen_proteins = [
    "nitrogen fixation protein NifB",
    "nitrogen fixation protein NifX",
    "nitrogen fixation protein NifZ",
    "nitrogen fixation protein NifT"
]
nitrogen_output_file = "nitrogen_fix_prot.tsv"

# Filtra linhas com os termos desejados na coluna 'KOfam '
filtered_nitrogen_df = filtered_df[filtered_df['KOfam'].isin(nitrogen_proteins)]

# Salva o filtro de proteínas de fixação de nitrogênio
filtered_nitrogen_df.to_csv(nitrogen_output_file, sep="\t", index=False)
print(f"Proteínas de fixação de nitrogênio salvas em: {nitrogen_output_file}")

# Etapa 3: Gerar arquivos para cada genoma
genomes = [
    "g_Dulcicalothrix_sp", "g_Fortiea_sp", "g_Rivularia_sp_i", "g_Rivularia_sp_ii",
    "s_336_3_sp", "s_Aulosira_anomala_i", "s_Aulosira_anomala_ii", "s_Aulosira_anomala_iii",
    "s_Aulosira_anomala_iv", "s_Calothrix_rhizosoleniae", "s_Dulcicalothrix_desertica",
    "s_NIES_3974", "s_Nostoc_muscorum", "s_PCC_6303", "s_Richelia_intracellularis",
    "s_Rivularia_radiosa"
]

# Filtra e cria arquivos para cada genoma
for genome in genomes:
    genome_df = filtered_nitrogen_df[filtered_nitrogen_df['genome_name'] == genome]
    genome_output_file = f"{genome}.tsv"
    genome_df.to_csv(genome_output_file, sep="\t", index=False)
    print(f"Arquivo para o genoma {genome} salvo como: {genome_output_file}")
