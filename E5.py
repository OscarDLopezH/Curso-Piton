##E5
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla 
# la <n> entre <m> da un cociente <c> y un resto <r> 
# donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
N1 = int(input("Ingresa un numero entero: \n "))
N2 = int(input("Ingresa otro numero entero: \n "))
c = N1/N2 
r = N1%N2
print("Cociente: ",int(c))
print("Residuo: ",int(r))