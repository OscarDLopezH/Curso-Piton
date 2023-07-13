##E14
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
# (desde 1 hasta su edad).

Edad = int(input("Ingresa tu edad:\n"))

for i in range(Edad): 
    print(f"{i+1}")
