import requests

#captura
def obtener_eventos(url, headers):
    # Hacer un get a la URL con los encabezados personalizados
    response = requests.get(url, headers=headers)
    eventos = []

    # Verificar el estado de la respuesta
    if response.status_code == 200:
        # Intentar obtener el JSON si la respuesta es exitosa
        try:
            data = response.json()
            data = data['events']

            for i in range(len(data)):
                # Tournament
                tournament = data[i]['tournament']
                name_tournament = tournament['name']

                # Season
                season = data[i]['season']
                year_season = season['year']

                # Round
                round_info = data[i]['roundInfo']
                round_number = round_info['round']

                # Id del evento
                id_event = data[i]['id']

                evento_info = {
                    'Torneo': name_tournament,
                    'Temporada': year_season,
                    'Ronda': round_number,
                    'Id': id_event
                }

                eventos.append(evento_info)
        except requests.exceptions.JSONDecodeError as e:
            print(f'Error al decodificar JSON: {e}')
    else:
        print(
            f'Error en la solicitud. Código de estado: {response.status_code}')
        print(response.text)

    return eventos
