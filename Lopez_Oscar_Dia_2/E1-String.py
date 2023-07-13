##E1 String
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla 
# en líneas distintas el nombre del usuario tantas veces como el número introducido.
Nombre = input("Ingresa tu nombre:\n")
Numero = abs(int(input("Ingresa un numero: \n ")))

for i in range(Numero): 
    print(f"{Nombre}")

