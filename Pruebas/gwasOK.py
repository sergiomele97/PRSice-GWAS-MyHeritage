import pandas as pd

# Cargar el archivo original
input_file = 'gwas_filtered.csv'  # Cambia esto al nombre de tu archivo
output_file = 'gwas.assoc'  # Cambia esto al nombre deseado para el archivo de salida

# Leer el archivo CSV
df = pd.read_csv(input_file)

# Extraer la información necesaria
df['A1'] = df['A1'].str.split('-').str[0]  # Obtener solo la parte antes del guion
df['A2'] = df['A1'].replace({'1': 'A', '2': 'B'})  # Cambia 1 y 2 a A y B según tu formato deseado

# Crear el nuevo DataFrame
new_df = pd.DataFrame({
    'SNP': df['A1'],
    'CHR': df['CHR'],
    'BP': df['BP'],
    'A1': df['A1'],
    'A2': df['A2'],
    'P': df['P'],
    'OR': df['OR']
})

# Guardar el nuevo DataFrame en un archivo
new_df.to_csv(output_file, sep=' ', index=False)

print(f"Archivo convertido guardado como {output_file}")
