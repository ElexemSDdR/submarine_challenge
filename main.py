from submarine import Submarine
import os
from pick import pick

def main() -> None:
    os.system("clear")
    submarine = None
    print("Bienvenido a 'Submarine creator', el creador de submarinos más piola hecho en Python. Ahora disponible en GitHub !!!. Vé a 'https://github.com/ElexemSDdR/submarine_challenge'.")
    print("Ingrese la opción que desee:")
    while True:
        print("1. Armar tu submarino\n2. Mostrar submarino\n3. Subir hasta la superficie\n4. Subir 15 metros\n5. Bajar 15 metros\n6. Ir hasta las profundidades\n7. Salir")
        options = input("Ingrese su opción: ")
        if not options.isdigit():
            print("Ingrese un número")
            continue
        else:
            options = int(options)
            if options == 1:
                submarine_possible_weapons = ["ninguna", "arpón", "cañon", "metralleta submarina"]
                submarine_name = input("Ingrese el nombre del submarino: ")
                submarine_color = input("Ingrese algún color para su submarino: ")

                while True:
                    submarine_current_deepness = input("Ingrese a qué profundidad (en metros) se encuentra su submarino: ")
                    if not submarine_current_deepness.isdigit():
                        print("Ingrese un número como nivel de profundidad")
                        continue
                    elif int(submarine_current_deepness) < 0 or int(submarine_current_deepness) > 545:
                        print("Ingrese un valor válido para su nivel de profundidad actual (545 metros como máximo)")
                        continue
                    else:
                        submarine_current_deepness = int(submarine_current_deepness)
                        break

                while True:
                    submarine_capacity = input("Ingrese la capacidad de gente que soporta su submarino (por defecto soporta a 20 personas, dejelo vacio para usar el valor por defecto): ")
                    if submarine_capacity == "":
                        submarine_capacity = 20
                        break
                    elif not submarine_capacity.isdigit():
                        print("Ingrese un número")
                        continue
                    else:
                        if int(submarine_capacity) < 20:
                            print("La capacidad mínima es de 20 personas")
                            continue
                        else:
                            submarine_capacity = int(submarine_capacity)
                            break

                submarine_weapon, index = pick(submarine_possible_weapons, "Elija si tiene algún arma posible o si no tiene: ", default_index = 0, indicator = "->>")

                if index == 0:
                    submarine_weapon = ""

                submarine = Submarine(submarine_name, submarine_color, submarine_current_deepness, submarine_capacity, submarine_weapon)
            elif options == 2:
                print(f"\n{submarine.__str__()}\n") if submarine != None else print("Primero cree un submarino")
            elif options == 3:
                print(f"\n{submarine.go_to_surface()}\n") if submarine != None else print("Primero cree un submarino")
            elif options == 4:
                print(f"\n{submarine.go_up()}\n") if submarine != None else print("Primero cree un submarino")
            elif options == 5:
                print(f"\n{submarine.go_down()}\n") if submarine != None else print("Primero cree un submarino")
            elif options == 6:
                print(f"\n{submarine.go_to_deepest()}\n") if submarine != None else print("Primero cree un submarino")
            elif options == 7:
                break


if __name__  == "__main__":
   main()
