##E12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
Frase = input("Ingresa una frase:\n ")
Letra = input("Ingrea la letra que deseas contar:\n ")
Conteo = Frase.count(Letra)
if (Conteo !=0):
    print(f"La letra: {Letra} aparece un total de {Conteo} veces")
else: 
    print(f"La letra: {Letra} no aparece, uy no")