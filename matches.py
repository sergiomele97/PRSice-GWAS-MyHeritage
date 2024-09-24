def load_snp_data(file_path):
    snp_data = {}
    with open(file_path, 'r') as f:
        for line in f:
            # Limpiar y dividir la línea
            parts = line.strip().replace('"', '').split(',')
            if len(parts) == 4:  # rsID, CHR, BP, A1
                snp_id = parts[0]
                snp_data[snp_id] = parts  # Guardar toda la línea con el SNP como clave
    return snp_data

def load_gwas_data(file_path):
    gwas_data = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 7:  # SNP CHR BP A1 A2 OR P
                snp_id = parts[0]
                gwas_data[snp_id] = parts  # Guardar toda la línea con el SNP como clave
    return gwas_data

def find_matches(snp_data, gwas_data):
    matches = {}
    for snp_id in snp_data:
        if snp_id in gwas_data:
            matches[snp_id] = {
                'snp': snp_data[snp_id],
                'gwas': gwas_data[snp_id]
            }
    return matches

def save_matches(matches, output_file):
    with open(output_file, 'w') as out:
        for snp_id, data in matches.items():
            out.write(','.join(data['snp']) + '\n')  # Guardar solo los datos SNP

def main():
    # Rutas de los archivos
    snp_file = 'MyHeritage_raw_dna_data.csv'  # Cambia esto por la ruta de tu archivo SNP
    gwas_file = 'matches_gwas.txt'   # Cambia esto por la ruta de tu archivo GWAS
    output_file = 'matched_snps.txt'  # Archivo de salida para coincidencias

    # Cargar datos
    snp_data = load_snp_data(snp_file)
    gwas_data = load_gwas_data(gwas_file)

    # Encontrar coincidencias
    matches = find_matches(snp_data, gwas_data)

    # Guardar coincidencias en un archivo
    if matches:
        save_matches(matches, output_file)
        print(f"Coincidencias guardadas en {output_file}.")
    else:
        print("No se encontraron coincidencias.")

if __name__ == "__main__":
    main()
