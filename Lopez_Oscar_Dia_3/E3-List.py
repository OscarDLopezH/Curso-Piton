##E3-List
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

Materias = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
Calificacion = []
Remover = []
for i in range(0,len(Materias)):
    Calificacion.append(int(input(f"Ingresa la calificacion de {Materias[i]}:")))
    if Calificacion[i]>5:
        Remover.append(Materias[i])
for i in Remover:
    Materias.remove(i)

print("Tendras que repetir: ")
for i in Materias: 
    print(i)

