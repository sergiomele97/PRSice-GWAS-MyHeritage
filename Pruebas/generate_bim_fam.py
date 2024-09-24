# Cargar el archivo CSV
csv_file = 'rawdata.csv'  # Cambia esto al nombre de tu archivo CSV

# Inicializar listas para almacenar los datos
data = []

# Leer el archivo CSV como texto
with open(csv_file, 'r') as file:
    for line in file:
        # Quitar saltos de línea y comillas
        line = line.strip().replace('"', '')
        # Dividir por comas
        parts = line.split(',')
        # Asegurarnos de que hay exactamente 4 partes
        if len(parts) == 4:
            data.append(parts)

# Convertir a DataFrame
import pandas as pd

df = pd.DataFrame(data, columns=['RSID', 'CHROM', 'POSITION', 'RESULT'])

# Verificar el contenido del DataFrame
print(df.head())  # Esto imprimirá las primeras filas del DataFrame

# Crear archivo .bim
bim_file = 'my_data.bim'
with open(bim_file, 'w') as bim:
    for index, row in df.iterrows():
        rsid = row['RSID']
        chrom = row['CHROM']
        position = row['POSITION']
        
        # Asignar alelos
        a1 = row['RESULT'][0]  # Primer alelo
        a2 = row['RESULT'][1] if len(row['RESULT']) > 1 else 'N'  # Segundo alelo
        
        # Escribir en el archivo .bim
        bim.write(f"{rsid}\t{chrom}\t{position}\t{a1}\t{a2}\n")

# Crear archivo .fam
fam_file = 'my_data.fam'
with open(fam_file, 'w') as fam:
    for i in range(len(df)):
        # Usar 1 como FID e IID y 0 para padre/madre, 1 para sexo (1=masculino)
        fam.write(f"1\t{i+1}\t0\t0\t1\t0\n")

print(f"Archivos {bim_file} y {fam_file} generados exitosamente.")
