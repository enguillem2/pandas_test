import requests

def obtener_geolocalizacion():
    # Realizar una solicitud a ipinfo.io para obtener datos de geolocalización
    respuesta = requests.get('http://ipinfo.io/json')
    datos = respuesta.json()

    # Extraer latitud y longitud
    if 'loc' in datos:
        latitud, longitud = datos['loc'].split(',')
        return float(latitud), float(longitud)
    else:
        return None


if __name__ == "__main__":
    # Obtener latitud y longitud
    latitud, longitud = obtener_geolocalizacion()
    print(f"Latitud: {latitud}, Longitud: {longitud}")
