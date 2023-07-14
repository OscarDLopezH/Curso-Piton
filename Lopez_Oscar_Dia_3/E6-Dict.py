##E6-Dict
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

Nombre = input("Ingresa tu nombre:\n")
Edad = int(input("Ingresa tu edad:\n"))
Direccion = input("Ingresa tu direccion:\n")
Telefono = input("Ingresa tu Telefono:\n") 

Datos = {"nombre":Nombre,"edad":Edad,"direccion":Direccion,"telefono":Telefono}
print(Datos["nombre"], "tiene", Datos["edad"], "años, vive en", Datos["direccion"], "y su número de teléfono es", Datos["telefono"]) 
