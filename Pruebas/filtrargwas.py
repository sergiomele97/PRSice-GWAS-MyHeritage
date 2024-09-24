import pandas as pd

# Lee el archivo de entrada
input_file = 'gwas-association-downloaded_2024-09-22-accessionId_GCST90328131.tsv'  # Cambia esto al nombre de tu archivo de entrada
output_file = 'gwas_filtered.csv'  # Cambia esto al nombre de tu archivo de salida

# Define las columnas que queremos extraer
columns_to_extract = {
    'SNP': 'SNP_ID_CURRENT',  # Cambia esto si el nombre de la columna es diferente
    'CHR': 'CHR_ID',
    'BP': 'CHR_POS',
    'A1': 'STRONGEST SNP-RISK ALLELE',
    'A2': 'MERGED',  # Si necesitas una segunda alela, asegúrate de que esta columna contenga la información correcta
    'P': 'P-VALUE',
    'OR': 'OR or BETA'
}

# Lee el archivo y selecciona las columnas necesarias
df = pd.read_csv(input_file, sep='\t')  # Cambia sep según el delimitador de tu archivo

# Filtra las columnas
filtered_df = df[list(columns_to_extract.values())]
filtered_df.columns = columns_to_extract.keys()  # Renombra las columnas

# Guarda el nuevo archivo en el formato requerido
filtered_df.to_csv(output_file, index=False)

print(f'Archivo filtrado guardado como {output_file}')
