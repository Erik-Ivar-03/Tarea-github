from palabras import obtener_palabra
from utils import mostrar_tablero, pedir_letra

def jugar():
    palabra_secreta = obtener_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6  # Número de intentos que tiene el jugador
    
    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        
        letra = pedir_letra()
        
        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.add(letra)

        if letra not in palabra_secreta:
            intentos_restantes -= 1
            print(f"¡Letra incorrecta! Te quedan {intentos_restantes} intentos.")
        else:
            print("¡Buena letra!")
            
        # Comprobar si el jugador ha adivinado la palabra
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("¡Felicidades, has ganado!")
            print("La palabra era:", palabra_secreta)
            break
    else:
        print("¡Te has quedado sin intentos! La palabra era:", palabra_secreta)
