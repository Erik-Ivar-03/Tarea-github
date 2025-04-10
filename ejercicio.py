import random

def adivina_el_numero():
    print("¡Bienvenido al juego de Adivina el Número!")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            adivinanza = int(input("Adivina un número entre 1 y 100: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    adivina_el_numero()  
