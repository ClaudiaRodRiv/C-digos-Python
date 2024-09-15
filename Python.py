"""
Python.py

Descripción:
Este script proporciona una visión general de conceptos básicos en Python.
Incluyendo operaciones aritméticas, manejo de variables, listas, condicionales, bucles, funciones, y la interacción con archivos. 
El script también muestra cómo utilizar módulos externos como `random` para generar números aleatorios.

Uso:
1. Imprime texto y realiza operaciones básicas como suma, resta, multiplicación y división.
2. Define y utiliza variables de diferentes tipos, incluyendo caracteres, cadenas, enteros, flotantes y booleanos.
3. Manipula listas, accede a sus elementos y determina su longitud.
4. Utiliza condicionales `if-else` para ejecutar código basado en condiciones.
5. Implementa bucles `for` para repetir bloques de código.
6. Define y utiliza funciones para realizar tareas específicas.
7. Muestra cómo leer y escribir en archivos utilizando los métodos `write` y `read`.
8. Importa y utiliza el módulo `random` para generar números aleatorios.

Asegúrate de ajustar las rutas de los archivos según tu entorno de trabajo. 
Este código sirve como una guía básica para comenzar a trabajar con Python y puede adaptarse a necesidades más específicas.

"""

# Imprimir texto
print("Texto a imprimir")

# Operaciones
a = 10
b = 5
# Suma
Suma = a + b
print("Suma:", Suma)
# Resta
Resta = a - b
print("Resta:", Resta)
# Multiplicación
Multiplicacion = a * b
print("Multiplicación:", Multiplicacion)
# División
Division = a / b
print("División:", Division)

# Variables
# Char
VariableChar = "Pablabra"
# String
VariableString = "Varias palabras"
# Int
VariableInt = 100
# Float
VariableFloat = 111.111
# Boolean
VariableBoolean = True

# Listas
NombreLista = ["Elemento1", "Elemento2", "Elemento3"]
# Imprimir lista
print("Lista:", NombreLista)
# Acceder a un elemento de la lista
print("Elemento 0 de la lista:", NombreLista[0])
# Longitud de la lista
print("Longitud de la lista:", len(NombreLista))

# Condicionales
# Los condicionales permiten ejecutar código en función de una condición.
# Condicional If - Else
Valor = input("Ingrese un valor:")
Valor = float(Valor)
# Condicionamos: Si el valor es mayor a 0
if Valor > 0:
    # Se cumple esta condición:
    print("El valor", Valor, "es positivo")
else:
    # Si no es mayor a 0, se cumple esta condición:
    print("El valor", Valor, "es negativo")

# Bucles
# Los bucles te permiten repetir un bloque de código varias veces.
# Bucle For
# La función range crea una serie de números consecutivos. Iniciando en 0 y terminando un número antes del argumento que se le entrega a la función.
for x in range(5):
    print("Bucle:", x)

# Funciones
# Las funciones son bloques de código reutilizables que realizan una tarea específica.
# Funcion para sumar dos valores
def FuncionSuma(a, b):
    return a + b
# Implementamos la función
print("Primera Suma:", FuncionSuma(10, 5))
print("Segunda Suma:", FuncionSuma(15, 80))
print("Tercera Suma:", FuncionSuma(60, 25))

# Leer y escribir Archivos
# Se puede interactuar con archivos en el sistema.
# Escribir
# w = El método write sobrescribirá cualquier cosa que el archivo contenga.
# a = El método append agregara un elemento de cualquier tipo al final de una lista.
# Ruta donde se encuentran el archivo .txt (reemplazar con la ruta adecuada)
Archivo = open("Ruta/Del/Directorio/DocumentoTexto.txt", "a")
Archivo.write("\n" + "Este texto se escribió mediante el código.")
Archivo.close()
# Leer
# r = El método read leerá todo el contenido de un archivo y lo devolverá como una cadena de texto.
# Ruta donde se encuentran el archivo .txt (reemplazar con la ruta adecuada)
Archivo = open("Ruta/Del/Directorio/DocumentoTexto.txt", "r")
print(Archivo.read())
Archivo.close()
# Módulos
# Modulo random
import random
# Definimos un rango de numeros
NumeroAleatorio = random.randint(1, 100)
print("Número aleatorio entre el 1 y el 100:", NumeroAleatorio)
