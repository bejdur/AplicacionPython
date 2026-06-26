import json
import requests

def guardar_datos(lista):
    with open("archivo.json", "w", encoding="utf-8") as i:
        json.dump(lista, i, indent=4)
def cargar_datos():
    with open("archivo.json", "r", encoding="utf-8") as i:
        return json.load(i)