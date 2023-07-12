##E6
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que pida al usuario el número de payasos y muñecas 
# que desea enviar y calcule el peso total del paquete que será enviado. La salida debe tener un formato:
# "Se enviaron <# muñecas> muñecas y <# payasos> payasos, con un peso total de <peso total>"

payasos = 112 
muñecas = 75

Num_payasos = int(input("ingresa el numero de payasos:\n "))
Num_muñecas = int(input("ingresa el numero de muñecas:\n "))

Peso_payasos = payasos*Num_payasos
Peso_muñecas = muñecas*Num_muñecas
print("Se enviaron", Num_muñecas, "muñecas y ",Num_payasos, "payasos, con un peso total de ",Peso_muñecas+Peso_payasos)
