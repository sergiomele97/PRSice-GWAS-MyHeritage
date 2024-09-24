# Nombre de tu archivo original
input_file = 'rawdata.csv'
# Nombre del archivo limpio que se creará
output_file = 'cleaned_data.csv'

# Abrir el archivo original y el nuevo archivo para escribir
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Reemplazar las comillas dobles y las comillas simples
        cleaned_line = line.replace('""', '"').replace('"', '').strip()
        # Escribir la línea limpia en el nuevo archivo
        outfile.write(cleaned_line + '\n')

print(f"Archivo {output_file} generado exitosamente.")
