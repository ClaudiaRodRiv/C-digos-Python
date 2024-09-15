import pandas as pd
import os
from tkinter import Tk, filedialog
from openpyxl import load_workbook

"""
FormatoDevoluciones.py
Este script se utiliza para generar archivos CSV a partir de un archivo Excel que contiene información de artículos. 
El formato generado es utilizado en el proceso de actualización de precios de artículos en mi entorno de trabajo.

Uso:
1. El usuario selecciona un archivo Excel y una carpeta de destino.
2. Se lee cada hoja del Excel.
3. Se genera un CSV para cada hoja del Excel, con un formato predefinido.
4. El archivo CSV se guarda en la carpeta seleccionada.

El formato del DataFrame utilizado para generar los archivos CSV está adaptado al formato específico que se utiliza en mi 
trabajo para la actualización de precios. Este formato puede ser modificado según las necesidades particulares de cada usuario. 
Puedes ajustar las columnas y los datos en el DataFrame según los requisitos específicos de tu sistema o proceso.

"""

# Función para seleccionar un archivo Excel
def seleccionar_excel():
    # Se abre un cuadro de diálogo para que el usuario seleccione el archivo Excel
    ruta_excel = filedialog.askopenfilename(title="Seleccionar Excel", filetypes=[("Excel files", "*.xlsx *.xls")])
    return ruta_excel

# Función para seleccionar la carpeta de destino
def seleccionar_carpeta():
    # Se abre un cuadro de diálogo para que el usuario seleccione la carpeta de destino para guardar los CSV
    ruta_carpeta = filedialog.askdirectory(title="Seleccionar carpeta de destino")
    return ruta_carpeta

# Función principal para procesar el Excel y generar los CSV
def procesar_excel(ruta_excel, ruta_carpeta):
    # Cargar el libro de Excel con openpyxl
    workbook = load_workbook(ruta_excel)
    # Obtener los nombres de todas las hojas en el Excel
    nombres_hojas = workbook.sheetnames

    # Iterar sobre cada hoja en el archivo Excel
    for nombre_hoja in nombres_hojas:
        hoja = workbook[nombre_hoja]

        # Crear un diccionario para almacenar los datos de la hoja actual en formato de columnas.
        # A continuación se especifica qué valores se colocarán en cada columna del archivo CSV que se va a generar.
        # Estos valores pueden ser ajustados según las necesidades del usuario.
        data = {
            'A': ['ParentKey', 'ItemCode'] + [hoja[f'A{i}'].value for i in range(2, hoja.max_row + 1)],  # Columna A: ParentKey, ItemCode, y datos de la columna A del Excel
            'B': ['LineNum', 'LineNum'] + [36] * (hoja.max_row - 1),  # Columna B: Valor fijo 36 para todas las filas
            'C': ['PriceList', 'PriceList'] + [37] * (hoja.max_row - 1),  # Columna C: Valor fijo 37 para todas las filas
            'D': ['Price', 'Price'] + [hoja[f'F{i}'].value for i in range(2, hoja.max_row + 1)],  # Columna D: Precios tomados de la columna F del Excel
            'E': ['Currency', 'Currency'] + ['$'] * (hoja.max_row - 1),  # Columna E: Valor fijo "$" para todas las filas
        }

        # Crear un DataFrame con pandas usando el diccionario de datos
        df = pd.DataFrame(data)

        # Definir la ruta y el nombre del archivo CSV que se generará
        ruta_csv = os.path.join(ruta_carpeta, f"Devoluciones Palacio {nombre_hoja}.csv")
        # Guardar el DataFrame como un archivo CSV, sin índices ni encabezados
        df.to_csv(ruta_csv, index=False, header=False)

    # Mensaje de confirmación cuando el proceso ha terminado
    print("Proceso completado.")

# Configurar la interfaz gráfica
def crear_interfaz():
    # Crear una ventana oculta usando Tkinter
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal ya que solo usaremos los cuadros de diálogo

    # Llamar a la función para seleccionar el archivo Excel
    ruta_excel = seleccionar_excel()
    if not ruta_excel:
        # Si no se selecciona un archivo, mostrar un mensaje y salir
        print("No se seleccionó ningún archivo Excel.")
        return

    # Llamar a la función para seleccionar la carpeta de destino
    ruta_carpeta = seleccionar_carpeta()
    if not ruta_carpeta:
        # Si no se selecciona una carpeta, mostrar un mensaje y salir
        print("No se seleccionó ninguna carpeta de destino.")
        return

    # Llamar a la función para procesar el archivo Excel y generar los CSV
    procesar_excel(ruta_excel, ruta_carpeta)

# Ejecutar la interfaz cuando se ejecuta el script directamente
if __name__ == "__main__":
    crear_interfaz()
