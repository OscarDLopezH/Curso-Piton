##E7-if
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú 
# con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

Vegetarianas = ["Pimiento","Tofu"]
NoVegetarianas = ["Peperoni", "Jamón","Salmón"]

Pizza = str(input("Deseas una pizza Vegetareana? [S/N]: \n"))
if (Pizza == 'S') or (Pizza =='s'):
    Opcion = int(input(f"Selecciona el ingrediente:\n1){Vegetarianas[0]}\n2){Vegetarianas[1]}\n"))
    print(f"Tu pieza es Vegetariana con {Vegetarianas[Opcion]} Con Mozzarella y tomate" )
else:
    Opcion = int(input(f"Selecciona el ingrediente:\n1){NoVegetarianas[0]}\n2){NoVegetarianas[1]}\n3){NoVegetarianas[2]}\n"))
    print(f"Tu pieza No es Vegetariana, tiene {NoVegetarianas[Opcion]} Con Mozzarella y tomate" )