import pandas as pd

# Cargar el archivo CSV
csv_file = 'rawdata.csv'  # Asegúrate de que este es el nombre correcto

try:
    # Leer el archivo CSV como texto
    with open(csv_file, 'r') as f:
        lines = f.readlines()

    # Procesar cada línea y limpiar los datos
    data = []
    for line in lines:
        # Quitar comillas y espacios extra
        line = line.replace('"', '').strip()
        # Dividir la línea por comas
        data.append(line.split(','))

    # Convertir a DataFrame
    df = pd.DataFrame(data)

    # Verificar si se cargaron los datos correctamente
    print("Datos cargados:")
    print(df.head())  # Muestra las primeras filas

    # Crear archivo .ped
    ped_file = 'my_data.ped'
    with open(ped_file, 'w') as ped:
        # Escribir la cabecera para un solo individuo (FID, IID)
        ped.write("1 1 0 0 0 0 ")

        # Verificar el número de filas
        print(f"Número de SNPs: {len(df)}")

        # Escribir los genotipos
        for index, row in df.iterrows():
            alleles = row[3]  # Acceder a la columna RESULT
            print(f"SNP {row[0]}: alelos = {alleles}")  # Imprimir alelos para depuración

            if pd.isna(alleles) or len(alleles) < 2:
                print(f"Error en SNP {row[0]}: alelos no válidos.")
                continue  # Saltar si los alelos no son válidos

            a1 = alleles[0]  # Primer alelo
            a2 = alleles[1]  # Segundo alelo
            ped.write(f"{a1} {a2} ")

        ped.write("\n")  # Nueva línea al final

    print(f"Archivo {ped_file} generado exitosamente.")

except Exception as e:
    print(f"Ocurrió un error: {e}")
