##E12
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
Salir = "salir"
Texto = ""
while Texto != Salir: 
    Texto = str(input("Escribe algo: "))
    if Texto == Salir: 
        break
    else:
        for i in range(3):
            print(f"{Texto}")

