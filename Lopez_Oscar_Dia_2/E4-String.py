##E4-String
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
Frase = input("Ingresa una frase: \n")
Vocal = input("Ingresa una vocal:\n")

print(Frase.replace(Vocal,Vocal.upper()))
