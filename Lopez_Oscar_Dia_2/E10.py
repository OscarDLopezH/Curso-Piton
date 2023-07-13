##E10
# Escribir un programa que pida al usuario un número entero positivo mayor que 2 y muestre por pantalla si es un número primo o no.
Numero = int(input("Ingresa un numero entero positivo mayor que 2:\n"))
if Numero>2: 
    if (Numero%2) == 0: 
        print(f"El Numero: {Numero} es Par :O\n") 
    elif (Numero%2 !=0): 
        print(f"El Numero: {Numero} es Impar\n")
else: 
    print(f"El Numero {Numero} no es mayor que 2, burro")
