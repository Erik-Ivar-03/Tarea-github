# utils.py

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra_secreta])
    print("Palabra: ", tablero)

def pedir_letra():
    letra = input("Ingresa una letra: ").lower()
    while len(letra) != 1 or not letra.isalpha():
        print("Por favor ingresa solo una letra.")
        letra = input("Ingresa una letra: ").lower()
    return letra
