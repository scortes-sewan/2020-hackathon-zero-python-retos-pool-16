from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player.lower() == ai.lower():
        return "Empate!"

# Entry Point
def Game():
    #
    #
    
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)

