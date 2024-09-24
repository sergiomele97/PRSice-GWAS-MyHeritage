def load_gwas_data(file_path):
    gwas_data = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 7:  # SNP CHR BP A1 A2 OR P
                snp_id = parts[0]
                gwas_data[snp_id] = parts  # Guardar toda la línea con el SNP como clave
    return gwas_data

def load_bim_data(file_path):
    bim_data = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 6:  # CHR SNP 0 BP 0 A1
                snp_id = parts[1]
                bim_data[snp_id] = parts  # Guardar toda la línea con el SNP como clave
    return bim_data

def find_matches(gwas_data, bim_data):
    matches = {}
    for snp_id in gwas_data:
        if snp_id in bim_data:
            matches[snp_id] = {
                'gwas': gwas_data[snp_id],
                'bim': bim_data[snp_id]
            }
    return matches

def save_matches(matches, gwas_output_file, bim_output_file):
    with open(gwas_output_file, 'w') as gwas_out, open(bim_output_file, 'w') as bim_out:
        for snp_id, data in matches.items():
            gwas_out.write('\t'.join(data['gwas']) + '\n')  # Escribir datos GWAS
            bim_out.write('\t'.join(data['bim']) + '\n')    # Escribir datos BIM

def main():
    # Rutas de los archivos
    gwas_file = 'dataset.txt'  # Cambia esto por la ruta de tu archivo GWAS
    bim_file = 'mybed.bim'      # Cambia esto por la ruta de tu archivo .bim
    gwas_output_file = 'matches_gwas.txt'  # Archivo de salida para coincidencias GWAS
    bim_output_file = 'matches_bim.bim'     # Archivo de salida para coincidencias BIM

    # Cargar datos
    gwas_data = load_gwas_data(gwas_file)
    bim_data = load_bim_data(bim_file)

    # Encontrar coincidencias
    matches = find_matches(gwas_data, bim_data)

    # Imprimir resultados y guardar en archivos
    if matches:
        print("Coincidencias encontradas:")
        for snp_id, data in matches.items():
            print(f"SNP: {snp_id}")
            print(f"  GWAS Data: {data['gwas']}")
            print(f"  BIM Data: {data['bim']}")
        
        # Guardar coincidencias en archivos
        save_matches(matches, gwas_output_file, bim_output_file)
        print(f"Coincidencias guardadas en {gwas_output_file} y {bim_output_file}.")
    else:
        print("No se encontraron coincidencias.")

if __name__ == "__main__":
    main()
