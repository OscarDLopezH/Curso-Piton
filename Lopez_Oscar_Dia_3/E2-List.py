##E2-List
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
Numeros = []
for i in range(1,11): 
    Numeros.append(i)
for i in range(1,len(Numeros)+1):
    print(Numeros[-i],end = ", ")