from captura import jugadores
from captura import jornadas
from captura import equipo
# Creamos un menu para que el usuario seleccione que desea hacer


def menu():
    print("1. Capturar jornadas")
    print("2. Capturar jugadores")
    print ("3. Capturar equipos")
    print("4. Salir")
    return int(input("Seleccione una opcion: "))


def main():
    opcion = menu()
    while opcion != 4:
        if opcion == 1:
            jornadas.main()
        elif opcion == 2:
            jugadores.main()
        elif opcion == 3:
            equipo.main()
        else:
            print("Opcion no válida")
        opcion = menu()


if __name__ == "__main__":
    main()

    print("Fin del programa")
