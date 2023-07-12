
##E7
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.

Primer = float(input("Ingresa la cantidad inicial depositada: \n"))
Segundo = float(input("Ingresa la cantidad del segundo año depositada: \n"))
Tercer = float(input("Ingresa la cantidad del tercer año depositada: \n"))
P1 = Primer+1.04
P2 = (P1+Segundo)*(1.04)
P3 = (P2+Tercer)*1.04
print("Primer año: ",round(P1,2))
print("Segundo año: ",round(P2,2))
print("Tercer año: ",round(P3,2))

