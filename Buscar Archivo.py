import os

Carpeta = input("Ingrese la carpeta: ")
Ruta = r'C:\Users\cprodriguez-ext\Documents\Lacoste\E-Commerce\DAT'

# Directorio donde se encuentran los archivos .dat
Directorio = os.path.join(Ruta, Carpeta)

# Texto a buscar
Buscar = "9016810"

# Recorrer todos los archivos en el directorio
for Archivo in os.listdir(Directorio):
    if Archivo.endswith(".dat"):
        filepath = os.path.join(Directorio, Archivo)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            # Leer el contenido del archivo
            Contenido = file.read()
            # Buscar el texto
            if Buscar in Contenido:
                print(f"El archivo {Archivo} contiene el texto {Buscar}")
