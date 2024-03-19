import requests
import datetime
from concurrent.futures import ThreadPoolExecutor
from dominio.Equipo import Equipos

def obtenerequipo(i, token):
     # Obtenemos los datos extra de mister
    payload = {
        'post': 'teams',
        'id': i,
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'X-Auth': '6baca5339d20a40b459ad851692e643f',
        'Cookie': f'token={token};'
    }
    
    url = "https://mister.mundodeportivo.com/ajax/sw"

    response = requests.post(url, data=payload, headers=headers)
    print(response.status_code)

    if response.status_code == 200:
        response = response.json()
        response = response['data']
        team = response['team']
        

        print(f"Procesando equipo {team['name']['id']}")
       

        response = requests.get(url, headers=headers)

       

        equipo = Equipos(
            id=team['id'],
            id_as=team['id_as'],
            id_biwenger=team['id_biwenger'],
            id_competition=team['id_competition'],
            teamLogoUrl=team['teamLogoUrl'],
            name=team['name'],
            updated=team['updated'],
          
        )
        
        print(f"Equipo {team['name']} ")
        print(equipo)
        equipo.insert_equipo()
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
                futures = [executor.submit(obtenerequipo, i, token)
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

    