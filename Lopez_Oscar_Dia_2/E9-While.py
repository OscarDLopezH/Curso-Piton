#3E9-While
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

Contraseña = input("Ingresa una contraseña:\n")
Pregunta = input("Ingresa nuevamente la contraseña:\n")

while( Pregunta != Contraseña):
    Pregunta = input("Ingresa nuevamente la contraseña:\n")

print("Contraseña Correcta!\n")    