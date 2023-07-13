##E15
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
# los números impares desde 1 hasta ese número separados por comas.
Numero = abs(int(input("Ingresa un numero entero positivo:\n")))
Lista_NumPares = []
for i in range(Numero):
    if (i%2!= 0): 
        Lista_NumPares.append(i)
print(f"Los numeros impares son: {Lista_NumPares}")
