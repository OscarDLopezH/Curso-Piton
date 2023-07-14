##E5
# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.


Numeros = [50, 75, 46, 22, 80, 65, 8]
print(f"La lista de numeros {Numeros}")

Numeros.sort()
print(f"El numero menor es: {Numeros[0]} y el mayor es: {Numeros[len(Numeros)-1]}")