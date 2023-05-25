import urllib.parse
import requests
import json

def calcular_distancia_duracion(origen, destino):
    url = 'https://www.mapquestapi.com/directions/v2/route'
    params = {
        'key': '0dQX0VejSj1qs6nZVxckJmNFmYtKCkQh',
        'from': origen,
        'to': destino,
        'unit': 'k'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        distancia = data['route']['distance']
        duracion = data['route']['formattedTime']
        return distancia, duracion
    else:
        print(f"Error al realizar la solicitud. Código de respuesta: {response.status_code}")
        return None, None

def calcular_combustible(distancia):
    rendimiento = 12.5  # Rendimiento de combustible en km/litro
    combustible = distancia / rendimiento
    return combustible

def obtener_instrucciones(origen, destino):
    url = 'https://www.mapquestapi.com/directions/v2/route'
    params = {
        'key': '0dQX0VejSj1qs6nZVxckJmNFmYtKCkQh',
        'from': origen,
        'to': destino,
        'unit': 'k',
        'narrativeType': 'text'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        instrucciones = data['route']['legs'][0]['maneuvers']
        return instrucciones
    else:
        print(f"Error al realizar la solicitud. Código de respuesta: {response.status_code}")
        return None

def imprimir_instrucciones(instrucciones):
    print("--- Guía de Viaje ---")
    for i, instruccion in enumerate(instrucciones, 1):
        print(f"Paso {i}: {instruccion['narrative']}")
        print(f"    Distancia: {instruccion['distance']:.2f} km")
        print(f"    Duración: {instruccion['formattedTime']}")
        print()

def imprimir_narrativa(origen, destino, distancia, duracion, combustible, instrucciones):
    horas, minutos, segundos = map(int, duracion.split(':'))

    print("--- Narrativa del Viaje ---")
    print(f"Ciudad de Origen: {origen}")
    print(f"Ciudad de Destino: {destino}")
    print(f"Distancia: {distancia:.2f} km")
    print(f"Duración: {horas} horas, {minutos} minutos, {segundos} segundos")
    print(f"Combustible requerido: {combustible:.2f} litros")
    print()
    imprimir_instrucciones(instrucciones)

# Programa principal
while True:
    origen = input("Ingrese la Ciudad de Origen (o 'q' para salir): ")
    if origen.lower() == 'q':
        break

    destino = input("Ingrese la Ciudad de Destino (o 'q' para salir): ")
    if destino.lower() == 'q':
        break

    distancia, duracion = calcular_distancia_duracion(origen, destino)
    if distancia is not None and duracion is not None:
        combustible = calcular_combustible(distancia)
        instrucciones = obtener_instrucciones(origen, destino)
        if instrucciones is not None:
            imprimir_narrativa(origen, destino, distancia, duracion, combustible, instrucciones)


       
