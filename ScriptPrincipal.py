from servicio.ConsultaPrueba import ConsultaPrueba
import sys
import os

# Obtener el directorio actual del script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Agregar el directorio raíz del proyecto al sys.path
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

# Crear una instancia de la clase ConsultaPrueba
consulta_prueba = ConsultaPrueba()

# Obtener jugadores españoles
jugadores_espanoles = consulta_prueba.obtener_jugadores_por_nacionalidad('España')

# Imprimir los jugadores encontrados
if jugadores_espanoles:
    for jugador in jugadores_espanoles:
        print(jugador)
else:
    print("No se encontraron jugadores españoles.")
