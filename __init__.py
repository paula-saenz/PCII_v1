from captura import jugadores
from captura import jornadas

# Creamos un menu para que el usuario seleccione que desea hacer


def menu():
    print("1. Capturar jornadas")
    print("2. Capturar jugadores")
    print("3. Salir")
    return int(input("Seleccione una opcion: "))


def main():
    opcion = menu()
    while opcion != 3:
        if opcion == 1:
            jornadas.main()
        elif opcion == 2:
            jugadores.main()
        else:
            print("Opcion no válida")
        opcion = menu()


if __name__ == "__main__":
    main()

    print("Fin del programa")
