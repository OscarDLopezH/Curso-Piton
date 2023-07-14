##E4
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


Letras = []
Palabra = input("Ingresa una palabra:\n")


for i in range(0,len(Palabra)):
    Letras.append(Palabra[i])
Letras.reverse()
Lista = Letras.copy()
Letras.reverse()
for i in range(0,len(Letras)):
    if (Letras[i] == Lista[i]): 
        Palindromo = True
    else:
        Palindromo = False
        break
if Palindromo:
    print(f"{Palabra} Es un palindromo")
else:
    print(f"{Palabra} NO es un palindromo")
