import requests
import datetime
from concurrent.futures import ThreadPoolExecutor

from dominio.Jugador import Jugador


# captura de datos a mister
# capa servicios, coger datos de la bbdd
# esta no hace falta separarl, tiene que tener un main que la llame
def process_player(i, token):
    # Obtenemos los datos extra de mister
    payload = {
        'post': 'players',
        'id': i,
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36',
        'X-Auth': '6baca5339d20a40b459ad851692e643f',
        'Cookie': f'token={token};'
    }
    url = "https://mister.mundodeportivo.com/ajax/sw"

    response = requests.post(url, data=payload, headers=headers)
    print(response.status_code)

    if response.status_code == 200:
        response = response.json()
        response = response['data']
        player = response['player']
        playerRepo = response['playerRepo']
        owners = response['owners']

        print(f"Procesando jugador {player['name']}")
        if len(owners) > 0:
            owners = owners[0]['id_uc_to']
        else:
            owners = None

        # Obtenemos los datos extra de sofascrore
        url = f'https://api.sofascore.com/api/v1/player/{playerRepo["sofaScoreId"]}/attribute-overviews'
        response = requests.get(url, headers=headers)

        attacking = None
        creativity = None
        defending = None
        tactical = None
        technical = None

        aerial = None
        anticipation = None
        ballDistribution = None
        saves = None
        tacticalGK = None
        if response.status_code == 200:
            response = response.json()
            response = response['playerAttributeOverviews'][0]
            if (response['position'] == 'G'):
                aerial = response['aerial']
                anticipation = response['anticipation']
                ballDistribution = response['ballDistribution']
                saves = response['saves']
                tacticalGK = response['tactical']
            else:
                attacking = response['attacking']
                creativity = response['creativity']
                defending = response['defending']
                tactical = response['tactical']
                technical = response['technical']

        url = f'https://api.sofascore.com/api/v1/player/{playerRepo["sofaScoreId"]}'

        response = requests.get(url, headers=headers)

        jerseyNumber = None
        preferredFoot = None
        contractUntil = None
        proposedMarketValue = None
        retired = False
        if response.status_code == 200:
            response = response.json()
            response = response['player']
            try:
                retired = response['retired']
            except:
                pass
            preferredFoot = response['preferredFoot']
            if not retired:
                try:
                    jerseyNumber = response['jerseyNumber']
                except:
                    pass
                try:
                    contractUntil = response['contractUntilTimestamp']
                    # Convertimos contractUntil a un datetime
                    contractUntil = datetime.datetime.fromtimestamp(
                        contractUntil)
                except:
                    pass
                try:
                    proposedMarketValue = response['proposedMarketValue']
                except:
                    pass

        url = f'https://api.sofascore.com/api/v1/player/{playerRepo["sofaScoreId"]}/national-team-statistics'

        response = requests.get(url, headers=headers)

        debutTimestampSeleccion = None
        idSeleccion = None
        if response.status_code == 200:
            response = response.json()
            if len(response['statistics']) > 0:
                response = response['statistics'][0]
                debutTimestampSeleccion = response['debutTimestamp']
                # Convertimos debutTimestampSeleccion a un datetime
                debutTimestampSeleccion = datetime.datetime.fromtimestamp(
                    debutTimestampSeleccion)
                team = response['team']
                idSeleccion = team['id']

        jugador = Jugador(
            name=player['name'],
            barter=None,
            bid=player['bid'],
            floor=player['floor'],
            height=player['height'],
            id_mister=player['id'],
            id_competition_mister=player['id_competition'],
            id_team_mister=player['id_team'],
            id_marca=player['m_id'],
            multiplier=player['multiplier'],
            nationality=player['nationality'],
            offer=player['offer']['input'],
            owner=owners,
            photoUrl=player['photoUrl'],
            position=player['position'],
            status=player['status'],
            video_frame=player['video_frame'],
            weight=player['weight'],
            id_as=playerRepo['asId'],
            birthday=playerRepo['birthday'],
            id_biwenger=playerRepo['biwengerId'],
            created=playerRepo['created'],
            id_gsm=playerRepo['gsmId'],
            id_opta=playerRepo['optaId'],
            id_rf=playerRepo['rfId'],
            id_sofascore=playerRepo['sofaScoreId'],
            updated=playerRepo['updated'],
            attacking=attacking,
            creativity=creativity,
            defending=defending,
            tactical=tactical,
            technical=technical,
            aerial=aerial,
            anticipation=anticipation,
            ballDistribution=ballDistribution,
            saves=saves,
            tacticalGK=tacticalGK,
            jerseyNumber=jerseyNumber,
            preferredFoot=preferredFoot,
            contractUntil=contractUntil,
            proposedMarketValue=proposedMarketValue,
            debutTimestampSeleccion=debutTimestampSeleccion,
            idSeleccion=idSeleccion,
            retired=retired
        )
        jugador.insert_into_database()
    else:
        print(
            f"Fallo al obtener los datos del jugador {i}. Código de estado: {response.status_code}")


def main():
    login_url = "https://mister.mundodeportivo.com/api2/auth/email"
    payload = {"email": "ismacorporation@gmail.com", "password": "b4b00n2023"}
    headers = {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36',
    }

    response = requests.post(login_url, json=payload, headers=headers)

    if response.status_code == 200:
        response = response.json()
        token = response['token']
        print(f"Autenticación exitosa. Token de sesión: {token}")

        url = "https://mister.mundodeportivo.com/api2/auth/external/exchange-token"
        payload = {"token": token}
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            print("Token válido")
            token = response.cookies['token']

            with ThreadPoolExecutor(max_workers=12) as executor:
                futures = [executor.submit(process_player, i, token)
                           for i in range(16202, 100000)]

                # Wait for all futures to complete
                for future in futures:
                    future.result()

        else:
            print(
                f"Fallo al verificar el token. Código de estado: {response.status_code}")
            print(f"Respuesta del servidor: {response.text}")

    else:
        print(f"Fallo al autenticar. Código de estado: {response.status_code}")
        print(f"Respuesta del servidor: {response.text}")


if __name__ == "__main__":
    main()
