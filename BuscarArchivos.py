import os

"""
BuscarArchivos.py

Descripción:
Este script busca un texto específico dentro de todos los archivos con extensión .dat en un directorio determinado. 
El usuario debe ingresar el nombre de la carpeta dentro del directorio base donde se encuentran los archivos .dat. 
El script recorre cada archivo .dat en la carpeta especificada, lee su contenido y verifica si el texto buscado está presente. 
Si el texto se encuentra, se imprime el nombre del archivo que contiene el texto.

Uso:
1. Modifique la variable 'Ruta' con la ruta base donde están ubicados los archivos .dat.
2. Ejecute el script e ingrese el nombre de la carpeta cuando se le solicite.
3. Defina el texto a buscar en la variable 'Buscar'.
4. El script imprimirá los nombres de los archivos .dat que contienen el texto buscado.

"""

# Solicitar al usuario el nombre de la carpeta donde se buscarán los archivos .dat
Carpeta = input("Ingrese la carpeta: ")

# Ruta base donde se encuentran los archivos .dat (reemplazar con la ruta adecuada)
Ruta = r'Ruta\Del\Directorio\Base'

# Crear la ruta completa al directorio de búsqueda concatenando la ruta base y la carpeta proporcionada por el usuario
Directorio = os.path.join(Ruta, Carpeta)

# Texto que se desea buscar dentro de los archivos .dat (reemplazar con el texto adecuado)
Buscar = "Texto a Buscar"

# Recorrer todos los archivos en el directorio especificado
for Archivo in os.listdir(Directorio):
    # Verificar si el archivo tiene la extensión .dat
    if Archivo.endswith(".dat"):
        # Construir la ruta completa al archivo
        filepath = os.path.join(Directorio, Archivo)
        
        # Abrir el archivo en modo lectura, ignorando errores de codificación
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            # Leer el contenido del archivo
            Contenido = file.read()
            
            # Verificar si el texto a buscar está en el contenido del archivo
            if Buscar in Contenido:
                # Imprimir el nombre del archivo que contiene el texto buscado
                print(f"El archivo {Archivo} contiene el texto {Buscar}")
