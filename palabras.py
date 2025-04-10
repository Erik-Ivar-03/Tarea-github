# palabras.py

import random

def obtener_palabra():
    ##palabras con las que se jugaran en el juego del ahorcado
    palabras = ["python", "desarrollador", "programacion", "computadora", "ahorcado"]
    return random.choice(palabras)
