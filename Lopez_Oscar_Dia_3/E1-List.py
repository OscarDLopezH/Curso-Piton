##E1-List 
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
# En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
Asignatura = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
Notas = []


def PreguntaCal(i): 
    Cal = int(input(f"Ingresa la calificacion de la materia de {Asignatura[i]}:\n"))
    return Cal 
def MuestraCal():
    global Notas
    for i in range(0,len(Asignatura)): 
        print(f"En {Asignatura[i]} has sacado {Notas[i]}")

for i in range(0,len(Asignatura)): 
    Notas.append(PreguntaCal(i))


MuestraCal()