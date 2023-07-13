##E5-if
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def Introduce_Alumno():
    Nombre = input(("Ingresa el nombre del Alumno: \n"))
    Sexo = input("Ingresa el Sexo del Alumno [M/F]:\n ")
    if(Sexo =='M'):
        if(ord(Nombre[0]) > ord('N')):
            print("Perteneces a la lista A")
        else:
            print("Perteneces a la lista B")
    elif(Sexo == 'F'): 
        if(ord(Nombre[0]) < ord('M')):
            print("Perteneces a la lista A")
        else:
            print("Perteneces a la lista B")
      
Introduce_Alumno()