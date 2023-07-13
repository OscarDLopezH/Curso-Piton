##E3-String
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
# muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
Correo = input("Ingresa tu correo Electronico:\n ")
Correo_Alternativo = Correo[:Correo.find('@')]+"@ceu.es"
print(f"Tu correo es: {Correo}\nTu correo Alternativo es: {Correo_Alternativo}")