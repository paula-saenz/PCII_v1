from concurrent.futures import ThreadPoolExecutor

from obtenerEventosPorJornada import obtener_eventos
from obtenerInfoGeneral import obtenerInfoGeneral
import time

# Agregar encabezados comunes de un navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Connection': 'keep-alive',
}

url_base = 'https://api.sofascore.com/api/v1/unique-tournament/8/season/52376/events/round/'
urls = [f'{url_base}{i}' for i in range(1, 39)]

time_start = time.time()
with ThreadPoolExecutor() as executor:
    resultados = list(executor.map(
        obtener_eventos, urls, [headers] * len(urls)))

# Una vez que se han obtenidos los ids de los eventos, se pueden utilizar para obtener información más detallada de cada evento
# Comenzamos obteniendo la infomación general de los eventos
# Url base para obtener información de un evento: https://api.sofascore.com/api/v1/event/{id_event}
# Se puede utilizar el mismo método obtener_eventos para obtener la información de un evento

# Obtener información adicional para cada ID de evento
ids_eventos = [evento['Id']
               for jornada_info in resultados for evento in jornada_info]

with ThreadPoolExecutor() as executor:
    executor.map(obtenerInfoGeneral, [
                 f'https://api.sofascore.com/api/v1/event/{id_event}' for id_event in ids_eventos], [headers] * len(ids_eventos))
time_end = time.time()
print(f'Tiempo total: {time_end - time_start} segundos')
