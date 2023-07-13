##E16
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta
# atrás desde ese número hasta cero separados por comas.

Numero = abs(int(input("Ingresa un numero entero positivo:\n")))
Lista_NumPares = []
for i in range(Numero+1): 
    Lista_NumPares.append(i)
print(f"El conteo desde el numero hasta atras es: {Lista_NumPares[::-1]}")
