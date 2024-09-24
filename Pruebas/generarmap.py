import pandas as pd

# Nombre de tu archivo CSV limpio
csv_file = 'cleaned_data.csv'
# Nombre del archivo .map que se generará
map_file = 'my_data.map'

# Leer el archivo CSV
data = pd.read_csv(csv_file, header=None)

# Verificar que hay 4 columnas
if data.shape[1] == 4:
    # Asignar nombres a las columnas
    data.columns = ['RSID', 'CHROM', 'POSITION', 'RESULT']
else:
    raise ValueError("El archivo no tiene el número correcto de columnas.")

# Crear el archivo .map
with open(map_file, 'w') as f:
    for index, row in data.iterrows():
        rsid = row['RSID']  # RSID
        chrom = row['CHROM']  # Cromosoma
        position = row['POSITION']  # Posición
        
        # Escribir en el archivo .map
        f.write(f"{chrom}\t{rsid}\t0\t{position}\n")

print(f"Archivo {map_file} generado exitosamente.")
