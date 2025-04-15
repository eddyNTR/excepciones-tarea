#Ejercicio 1 – Conversión múltiple de datos Tenés una lista con distintos tipos de datos. Intentá convertir cada uno a entero, y capturá los errores correspondientes.

"""datos = ["123", "hola", 45.6, None, "999"]

for valor in datos:
    try:
        entero = int(valor)
        print(f"conversion exitosa: {entero}")
    except ValueError as es:
        print(f"No se puede converit {valor} a entero {es}")
    except TypeError as l:
        print(f"Tipo invalido para conversion: {valor} {l}")"""

#Ejercicio 2 – División segura Pedí al usuario dos números y realizá una división. Manejá los siguientes errores: División por cero Entrada inválida (no numérica)

"""num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")

try:
    resultado = int(num1) / int(num2)
    print(f"El resultado de la division es: {resultado}")
except ZeroDivisionError as p:
    print("Error: Division por cero no es permitida {p}")
except ValueError as a: 
    print("Error: Entrada invalida, ingrese un numero {a}")"""

#Ejercicio 3 – Acceso a lista segura Creá una lista de 5 elementos. Pedí al usuario un índice y mostrá el valor. Manejá IndexError y TypeError.

elementos = ["Python", "Java", "C++", "Ruby", "Go"]

try:
    indice = input("Ingrese un indice (0 a 4): ")
    print(f"El elemento en el indice {indice} es: {elementos[indice]}")
except IndexError as e:
    print(f"Error: Indice fuera de rango {e}")
except TypeError as o:
    print(f"Error: tipo de dato invalido {o}")