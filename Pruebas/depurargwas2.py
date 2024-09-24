import pandas as pd
import re

# Leer el archivo de entrada
input_file = 'input.txt'  # Cambia esto por el nombre de tu archivo de entrada
output_file = 'dataset.txt'  # Nombre del archivo de salida

# Leer el archivo como un DataFrame
df = pd.read_csv(input_file, sep='\t')

# Procesar el DataFrame para crear el nuevo formato
def extract_snp_info(row):
    # Extraer el SNP y el alelo efectivo
    snp = row['riskAllele'].split('-')[0]
    a1 = row['riskAllele'].split('-')[1] if '-' in row['riskAllele'] else '?'
    
    # Obtener el cromosoma y la posición, con manejo de errores
    try:
        chr_number, bp = row['locations'].split(':')
    except ValueError:
        chr_number = 'NA'  # O cualquier valor por defecto que quieras usar
        bp = 'NA'
    
    # Obtener OR desde orValue o beta como alternativa
    or_value = row['orValue']
    if or_value == '-' or pd.isna(or_value):
        beta_value = row['beta']  # Usar beta como alternativa
        if pd.notna(beta_value) and beta_value != '-':
            # Extraer el número del string usando una expresión regular
            match = re.search(r"[-+]?\d*\.\d+|\d+", beta_value)
            if match:
                or_value = float(match.group(0))  # Convertir a float
            else:
                or_value = 1.0  # Valor por defecto si no se encuentra un número
        else:
            or_value = 1.0  # Valor por defecto si beta también está vacío
    else:
        or_value = float(or_value)  # Convertir a float
        or_value = f"{or_value:.20f}"  # Formatear a string sin notación exponencial

    # Manejo de pValue, convirtiendo a string si es necesario
    p_value = row['pValue']
    if isinstance(p_value, str):
        try:
            p_value = float(p_value.replace('E', 'e'))  # Convertir a decimal
            p_value = f"{p_value:.20f}"  # Formatear a string sin notación exponencial
        except ValueError:
            p_value = None
    elif isinstance(p_value, float):
        p_value = f"{p_value:.20f}"  # Ya es un float, formatear a string

    # Asumir el alelo alternativo (ajustar según sea necesario)
    a2 = 'A' if a1 == 'C' else 'C'
    
    return pd.Series([snp, chr_number, bp, a1, a2, or_value, p_value])

# Aplicar la función a cada fila
new_df = df.apply(extract_snp_info, axis=1)
new_df.columns = ['SNP', 'CHR', 'BP', 'A1', 'A2', 'OR', 'P']

# Guardar el nuevo DataFrame en un archivo delimitado por espacios
new_df.to_csv(output_file, sep=' ', index=False)

# Mensaje de éxito
print(f'Archivo creado: {output_file}')
