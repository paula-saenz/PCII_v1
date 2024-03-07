import requests

# Definir la URL del endpoint de inicio de sesión
login_url = "https://mister.mundodeportivo.com/api2/auth/email"

# Definir la carga útil (payload) con las credenciales
payload = {"email": "ismacorporation@gmail.com", "password": "b4b00n2023"}

headers = {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36',

}

# Realizar la solicitud POST para autenticarse
response = requests.post(login_url, json=payload, headers=headers)

# Verificar si la autenticación fue exitosa
if response.status_code == 200:
    # Obtener el token de sesión de la respuesta
    response = response.json()
    token = response['token']
    print(f"Autenticación exitosa. Token de sesión: {token}")

    # Realizamos la segunda solicitud para verificar que el token sea válido
    url = "https://mister.mundodeportivo.com/api2/auth/external/exchange-token"
    payload = {"token": token}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Token válido")
        token = response.cookies['token']

        url = "https://mister.mundodeportivo.com/ajax/sw"
        # Payload para obtener información de un jugador
        payload = {
            'post': 'players',
            'id': '48684',
            'slug': 'robert-lewandowski',
            'clone': '0',
            'comments': '0'
        }

        # Payload para obtener información de un usuario
        payload = {
            'post': 'users',
            'id': 12685406,
            'slug': 'admin',
            'clone': 0,
            'comments': 0
        }

        # Payload para obtener información de todos los jugadores
        payload = {
            'post': 'players',
            'filters[position]': 0,
            'filters[value]': 0,
            'filters[team]': 0,
            'filters[injured]': 0,
            'filters[favs]': 0,
            'filters[owner]': 0,
            'filters[benched]': 0,
            'offset': 0,
            'order': 0,
            'name': '',
            'filtered': 0,
            'parentElement': '.sw-content'
        }

        headers['X-Auth'] = '6baca5339d20a40b459ad851692e643f'
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers[
            'Cookie'] = f'token={token};'
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            response = response.json()
            response = response['data']
            print(response)

        # Luego tenemos la información detallada de cada jugador por jornada
        url = "https://mister.mundodeportivo.com/ajax/player-gameweek"
        payload = {
            'id_gameweek': 2542,
            'id_player': 48684
        }

        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            response = response.json()
            response = response['data']
            print(response)
    else:
        print(
            f"Fallo al verificar el token. Código de estado: {response.status_code}")
        print(f"Respuesta del servidor: {response.text}")
else:
    print(f"Fallo al autenticar. Código de estado: {response.status_code}")
    print(f"Respuesta del servidor: {response.text}")
