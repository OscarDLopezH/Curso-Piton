##E6-if
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere 
# calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5 pesos y si es mayor de 18 años, 10 pesos.
Mensaje =["Entrada Gratis", "Debe pagar 5 pesos", "Debe pagar 10 pesos"]
Edad = int(input("Ingresa tu edad: \n")) 
if Edad < 4: 
    print(Mensaje[0])
elif (Edad > 4) and (Edad < 18):  
    print(Mensaje[1])
elif (Edad>18): 
    print(Mensaje[2])
    
