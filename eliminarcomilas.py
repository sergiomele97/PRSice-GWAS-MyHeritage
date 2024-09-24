# Abrir el archivo de salida para escribir
with open('myheritage_cleaned.txt', 'w') as out_file:
    # Abrir el archivo original como texto plano
    with open('MyHeritage_raw_dna_data.csv', 'r') as in_file:
        # Leer cada línea del archivo original
        for line in in_file:
            # Eliminar las comillas dobles y las comas adicionales
            cleaned_line = line.replace('"', '').replace(',"', ' ').replace(',', ' ')
            
            # Escribir la línea limpia en el archivo de salida
            out_file.write(cleaned_line)
