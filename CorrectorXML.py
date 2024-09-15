import tkinter as tk
from tkinter import ttk
import xml.etree.ElementTree as ET

"""
CorrectorXML.py
Este script se utiliza para corregir archivos XML generados de órdenes en temporada de descuentos, 
los cuales pueden tener errores de códigos de descuento duplicados. El objetivo del script es unificar los códigos de descuento 
duplicados para que los XML puedan viajar entre plataformas correctamente, evitando la necesidad de corrección manual.

Uso:
1. El usuario ingresa el contenido del XML en el cuadro de texto de entrada.
2. El script procesa el XML para unificar los descuentos duplicados.
3. El XML corregido se muestra en el cuadro de texto de salida.
4. El usuario puede copiar el XML corregido al portapapeles para su uso posterior.

El formato del XML utilizado para la corrección está adaptado al formato específico que se utiliza en mi entorno de trabajo.
Puedes ajustar las funciones y el procesamiento del XML según los requisitos específicos de tu sistema o proceso.

"""

def CorregirXML(xmlString):
    # Parsear la cadena XML
    Raiz = ET.fromstring(xmlString)

    # Iterar a través de cada OrderLine
    for LineaOrden in Raiz.findall('.//OrderLine'):
        DetallesDescuento = LineaOrden.find('DiscountDetails')
        
        if DetallesDescuento is None:
            continue

        # Encontrar todos los detalles de descuentos
        Descuentos = DetallesDescuento.findall('DiscountDetail')
        
        # Diccionario para almacenar las sumas de descuentos
        SumasDescuentos = {}
        ParaEliminar = []
        
        for Descuento in Descuentos:
            IdDetalleDescuento = Descuento.find('ExtDiscountDetailId').text
            MontoDescuento = float(Descuento.find('DiscountAmount').text)
            
            if IdDetalleDescuento in SumasDescuentos:
                SumasDescuentos[IdDetalleDescuento] += MontoDescuento
                ParaEliminar.append(Descuento)
            else:
                SumasDescuentos[IdDetalleDescuento] = MontoDescuento
        
        # Eliminar elementos duplicados
        for Descuento in ParaEliminar:
            DetallesDescuento.remove(Descuento)
        
        # Actualizar los elementos restantes con las sumas de descuentos
        for Descuento in DetallesDescuento.findall('DiscountDetail'):
            IdDetalleDescuento = Descuento.find('ExtDiscountDetailId').text
            Descuento.find('DiscountAmount').text = str(SumasDescuentos[IdDetalleDescuento])
    
    # Convertir el árbol XML de nuevo a una cadena
    return ET.tostring(Raiz, encoding='utf-8').decode('utf-8')

def AlHacerClicEnBotonCorregir():
    # Obtener la entrada del cuadro de texto
    XMLInput = CuadroTextoEntrada.get("1.0", "end-1c")
    # Corregir el XML
    XMLCorregido = CorregirXML(XMLInput)
    # Limpiar el cuadro de texto de salida
    CuadroTextoSalida.delete("1.0", "end")
    # Insertar el XML corregido en el cuadro de texto de salida
    CuadroTextoSalida.insert("1.0", XMLCorregido)
    # Limpiar el cuadro de texto de entrada
    CuadroTextoEntrada.delete("1.0", "end")

def AlHacerClicEnBotonCopiar():
    # Copiar el contenido del cuadro de texto de salida al portapapeles
    Raiz.clipboard_clear()
    Raiz.clipboard_append(CuadroTextoSalida.get("1.0", "end-1c"))

# Crear la ventana principal
Raiz = tk.Tk()
Raiz.title("Corrector de XML")

# Crear y colocar la etiqueta y el cuadro de texto de entrada
EtiquetaEntrada = ttk.Label(Raiz, text="Entrada XML:")
EtiquetaEntrada.grid(row=0, column=0, padx=10, pady=10)
CuadroTextoEntrada = tk.Text(Raiz, height=20, width=80)
CuadroTextoEntrada.grid(row=1, column=0, padx=10, pady=10)

# Crear y colocar la etiqueta y el cuadro de texto de salida
EtiquetaSalida = ttk.Label(Raiz, text="XML Corregido:")
EtiquetaSalida.grid(row=0, column=1, padx=10, pady=10)
CuadroTextoSalida = tk.Text(Raiz, height=20, width=80)
CuadroTextoSalida.grid(row=1, column=1, padx=10, pady=10)

# Crear y colocar el botón de corregir
BotonCorregir = ttk.Button(Raiz, text="Corregir XML", command=AlHacerClicEnBotonCorregir)
BotonCorregir.grid(row=2, column=0, pady=10)

# Crear y colocar el botón de copiar al portapapeles
BotonCopiar = ttk.Button(Raiz, text="Copiar al portapapeles", command=AlHacerClicEnBotonCopiar)
BotonCopiar.grid(row=2, column=1, pady=10)

# Iniciar el bucle principal de eventos
Raiz.mainloop()
