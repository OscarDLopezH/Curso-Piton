##E11
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
Palabra = input("Ingresa una palabra:\n")
for i in range(len(Palabra)):
    print(f"{Palabra[-i-1]}")





