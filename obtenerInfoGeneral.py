import requests

#captura clase funciones
def obtenerInfoGeneral(url, headers):
    # Hacer un get a la URL con los encabezados personalizados
    response = requests.get(url, headers=headers)
    eventos = []

    # Verificar el estado de la respuesta
    if response.status_code == 200:
        # Intentar obtener el JSON si la respuesta es exitosa
        try:
            data = response.json()
            data = data['event']

            # Venue (Estadio)
            venue = data['venue']
            venue_name = venue['stadium']['name']

            # Referee (Árbitro)
            referee = data['referee']
            referee_name = referee['name']
            yellow_cards = referee['yellowCards']
            red_cards = referee['redCards']
            yellow_red_cards = referee['yellowRedCards']
            referee_games = referee['games']

            # Equipo local
            home_team = data['homeTeam']
            home_team_name = home_team['name']
            home_team_manager = home_team['manager']['name']

            # Equipo visitante
            away_team = data['awayTeam']
            away_team_name = away_team['name']
            away_team_manager = away_team['manager']['name']

            evento_info = {
                'Estadio': venue_name,
                'Árbitro': referee_name,
                'Tarjetas Amarillas': yellow_cards,
                'Tarjetas Rojas': red_cards,
                'Tarjetas Amarillas y Rojas': yellow_red_cards,
                'Partidos Arbitrados': referee_games,
                'Equipo Local': home_team_name,
                'Entrenador Local': home_team_manager,
                'Equipo Visitante': away_team_name,
                'Entrenador Visitante': away_team_manager
            }
            eventos.append(evento_info)
        except requests.exceptions.JSONDecodeError as e:
            print(f'Error al decodificar JSON: {e}')
    else:
        print(
            f'Error en la solicitud. Código de estado: {response.status_code}')
        print(response.text)

    return eventos
