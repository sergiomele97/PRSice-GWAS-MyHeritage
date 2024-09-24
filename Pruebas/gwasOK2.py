import pandas as pd

# Cargar el archivo CSV
input_file = 'gwas.assoc'  # Cambia el nombre del archivo de entrada
output_file = 'gwas2.assoc'  # Nombre del archivo de salida

# Leer el archivo
df = pd.read_csv(input_file, delim_whitespace=True)

# Renombrar columnas
df.columns = ['SNP', 'CHR', 'BP', 'A1', 'A2', 'P', 'OR']

# Eliminar los .0 de la columna CHR y BP
df['CHR'] = df['CHR'].astype(int)
df['BP'] = df['BP'].astype(int)

# Guardar el nuevo archivo
df.to_csv(output_file, index=False, sep=' ')

print(f"Archivo procesado y guardado como {output_file}.")
