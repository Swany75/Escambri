#!/usr/bin/env python3

import os
import random
from colorama import Fore, Style

""" 
Ascii Art template
╔═╦═╗
║ ║ ║
╠═╬═╣
╚═╩═╝
"""

### CONSTANTS & VARIABLES #############################################################################

FAMILIES = ['Oros', 'Bastos', 'Espases', 'Copes']
CARTES = ['As', 'Dos', 'Tres', 'Quatre', 'Cinc', 'Sis', 'Set', 'Sota', 'Cavall', 'Rei']

### CLASSES ###########################################################################################

class Carta:
    def __init__(self, family, carta, value):
        self.family = family
        self.carta = carta
        self.value = value
    
    def get_color(self):
        # Assigna un color segons la família de la carta.
        colors = {
            'Oros': Fore.YELLOW,
            'Bastos': Fore.GREEN,
            'Espases': Fore.BLUE,
            'Copes': Fore.RED
        }
        return colors.get(self.family, Fore.WHITE)  # Color per defecte: blanc
        
    def __str__(self):
        return f"{self.carta} de {self.family} que te un Valor de: {self.value}"


class Player:
    def __init__(self, name):
        self.name = name
        self.cartes = []
        self.puntuacio = 0
    
    def addCard(self, carta):
        self.cartes.append(carta)
    
    def remCard(self, carta):
        self.cartes.remove(carta)
    
    def __str__(self):
        return "\n".join(str(carta) for carta in self.cartes)

class Escambri:
    def __init__(self):
        self.deck = []
        self.players = []
        self.triumph = None
        self.order = []
        
    def createDeck(self):
        for familia in FAMILIES:
            for carta in CARTES:
                valor = self.checkValue(carta)
                card = Carta(familia, carta, valor)
                self.deck.append(card)
        random.shuffle(self.deck)
    
    def checkValue(self, carta):
        values = {
            'As': 11, 'Dos': 0, 'Tres': 10, 'Quatre': 0, 'Cinc': 0,
            'Sis': 0, 'Set': 0, 'Sota': 2, 'Cavall': 3, 'Rei': 4
        }
        return values[carta]
    
    def addPlayer(self, name):
        self.players.append(Player(name))
    
    def startPlayer(self):
        start_id = random.randint(0, len(self.players) - 1)
        self.order = ordre(start_id, len(self.players))
        return self.players[start_id]
    
    def reparteix(self):
        for player in self.players:
            for _ in range(3):
                player.addCard(self.deck.pop(0))
        self.triumph = self.deck.pop(0)
        self.deck.append(self.triumph)


### FUNCIONS GENERALS #################################################################################

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pressToContinue():
    input("\nPulsa per continuar >>>")

### FUNCIONS ASCII ART ################################################################################

def printTitle():
    
    print("""
███████╗███████╗ ██████╗ █████╗ ███╗   ███╗██████╗ ██████╗ ██╗
██╔════╝██╔════╝██╔════╝██╔══██╗████╗ ████║██╔══██╗██╔══██╗██║
█████╗  ███████╗██║     ███████║██╔████╔██║██████╔╝██████╔╝██║
██╔══╝  ╚════██║██║     ██╔══██║██║╚██╔╝██║██╔══██╗██╔══██╗██║
███████╗███████║╚██████╗██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║██║
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝
    """)

### FUNCIONS DEL JOC ##################################################################################

def ordre(start_id, num_players):
    return [(start_id + i) % num_players for i in range(num_players)]

def setPlayers(joc):
    
    printTitle()
    
    while True:
        try:
            num_players = int(input("Introdueix el nombre de jugadors (0..4): "))
            if 0 <= num_players <= 4:
                for i in range(1, num_players + 1):
                    while True:
                        name = input(f"Jugador {i} escriu el teu nom: ")
                        if name.strip():
                            joc.addPlayer(name)
                            break
                        else:
                            print("El nom del jugador no pot estar buit")
                for i in range(num_players + 1, 5):
                    joc.addPlayer(f"Bot {i - num_players}")
                break
            print("Error: Introdueix un numero valid (0..4)") 
        except ValueError:
            print("Error: Introdueix un numero valid (0..4)")

    joc.createDeck()
    joc.reparteix()
    joc.startPlayer()
    
def player_score(player, players):
    return -player.puntuacio, players.index(player)

def generatePlayedCardsStr(playedCards):
    if playedCards:
        return "\n".join(
            f"║  {calcSpaces(f'{i + 1}) {carta.get_color()}{carta.carta} de {carta.family}{Style.RESET_ALL}', 41)}║  {calcSpaces(str(carta.value), 5)}║"
            for i, carta in enumerate(playedCards)
        )
    return "║                                  ║       ║"

def drawBoard(game, player, playedCards):
    clear()
    played_cards_str = generatePlayedCardsStr(playedCards)
    
    print(f"""
╔══════════════════════════════════════════╗
║ Triumph: {calcSpaces(str(f"{game.triumph.get_color()}{game.triumph.carta} de {game.triumph.family}{Style.RESET_ALL}"), 41)}║
╠═══════════════╦══════════════════╦═══════╣
║ Cartes en Joc ║                  ║ Valor ║
╠═══════════════╝                  ╠═══════╣
║                                  ║       ║
{played_cards_str}
║                                  ║       ║
╠══════════════════════════════════╩═══════╣
║ Torn {calcSpaces(f'de {player.name}', 36)}║
╠══════════════════════════════════╦═══════╣
║                                  ║       ║
{chr(10).join(f"║  {calcSpaces(f'{i + 1}) {carta.get_color()}{carta.carta} de {carta.family}{Style.RESET_ALL}', 41)}║  {calcSpaces(str(carta.value), 5)}║" for i, carta in enumerate(player.cartes))}
║                                  ║       ║
╚══════════════════════════════════╩═══════╝
""")
    playedCard = playCard(player)
    return playedCard

def finalBoard(game, playedCards, player_cards):
    clear()
    played_cards_str = generatePlayedCardsStr(playedCards)
    
    # Determinar el guanyador de la ronda
    winning_card = roundWinner(playedCards, game)
    winner = player_cards[winning_card]
    
    # Sumar els punts de les cartes jugades al guanyador
    winner_points = sum(carta.value for carta in playedCards)
    winner.puntuacio += winner_points
    
    game.order = ordre(game.players.index(winner), len(game.players))
    
    sorted_players = sorted(game.players, key=lambda p: player_score(p, game.players))
    players_str = "\n".join(
        f"║  {calcSpaces(f'{i + 1}) {player.name}', 32)}║  {calcSpaces(str(player.puntuacio), 5)}║"
        for i, player in enumerate(sorted_players)
    )
    
    print(f"El guanyador de la ronda és {winner.name} amb la carta {winning_card.carta} de {winning_card.family}")
    print(f"Ha guanyat {winner_points} punts aquesta ronda.")
    
    print(f"""
╔══════════════════════════════════════════╗
║ Triumph: {calcSpaces(str(f"{game.triumph.get_color()}{game.triumph.carta} de {game.triumph.family}{Style.RESET_ALL}"), 41)}║
╠═══════════════╦══════════════════╦═══════╣
║ Cartes en Joc ║                  ║ Valor ║
╠═══════════════╝                  ╠═══════╣
║                                  ║       ║
{played_cards_str}
║                                  ║       ║
╠════════════╦═════════════════════╬═══════╣
║ Torn Final ║                     ║ Punts ║
╠════════════╝                     ╠═══════╣
║                                  ║       ║
{players_str}
║                                  ║       ║
╚══════════════════════════════════╩═══════╝
""")
    print("Final de la ronda")
    pressToContinue()

def botPlayCard(player):

    played_card = player.cartes[0]
    
    for card in player.cartes:
        if card.value > played_card.value:
            played_card = card
    
    print(f"{player.name} ha jugat {played_card}")
    pressToContinue()
    
    return played_card

def playCard(player):
    
    if "Bot" in player.name or len(player.cartes) == 1:
        return botPlayCard(player)
    
    else:
        while True:
            try:
                card = int(input("Tria una carta per jugar: "))
                if 1 <= card <= len(player.cartes):
                    break
                print(f"Error: Introdueix un numero valid (1..{len(player.cartes)})")
            except ValueError:
                print(f"Error: Introdueix un numero valid (1..{len(player.cartes)})")

        print(f"Has jugat {player.cartes[card - 1]}")
        pressToContinue()
        return player.cartes[card - 1]

def calcSpaces(text, maxlen):
    lenText = len(text)
    espais = maxlen - lenText
    
    if espais > 0:
        return text + " " * espais
    return text[:maxlen]
    
def roundWinner(playedCards, game):    
    
    winning_card = playedCards[0]
    winning_value = winning_card.value
    
    for carta in playedCards:
        
        adjusted_value = carta.value
        
        if carta.family == game.triumph.family:
            adjusted_value *= 3
            
        if adjusted_value > winning_value:
            winning_card = carta
            winning_value = adjusted_value
            
    return winning_card

def GameOver(guanyador):
    
    clear()
    
    print(f"""
       ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████       ▄██████▄   ▄█    █▄     ▄████████    ▄████████ 
      ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███ 
      ███    █▀    ███    ███ ███   ███   ███   ███    █▀       ███    ███ ███    ███   ███    █▀    ███    ███ 
     ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄          ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
    ▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀          ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
      ███    ███   ███    ███ ███   ███   ███   ███    █▄       ███    ███ ███    ███   ███    █▄  ▀███████████ 
      ███    ███   ███    ███ ███   ███   ███   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███ 
      ████████▀    ███    █▀   ▀█   ███   █▀    ██████████       ▀██████▀   ▀██████▀    ██████████   ███    ███

                                  Enhorabona {guanyador.name} has guanyat amb {guanyador.puntuacio} punts
    """)

    pressToContinue()
    clear()

def get_score(player):
    return player.puntuacio

### MAIN CODE #########################################################################################

def main():
    
    clear()
    game = Escambri()
    WINNER = None

    setPlayers(game)
    player = game.startPlayer()

    clear()
    print(f"Comença el jugador {player.name}")
    pressToContinue()

    while any(player.cartes for player in game.players):
        playedCards = []
        player_cards = {}
        
        # Comprovar si queda només una carta a la mà de cada jugador
        if all(len(player.cartes) == 1 for player in game.players):
            for player in game.players:
                played_card = player.cartes.pop(0)
                playedCards.append(played_card)
                player_cards[played_card] = player
            finalBoard(game, playedCards, player_cards)
            break

        for player_index in game.order:
            current_player = game.players[player_index]
            
            if current_player.cartes:
                played_card = drawBoard(game, current_player, playedCards)
                playedCards.append(played_card)
                player_cards[played_card] = current_player
                current_player.cartes.remove(played_card)
            
                if game.deck:
                    current_player.cartes.append(game.deck.pop(0))

        finalBoard(game, playedCards, player_cards)

        if game.deck:
            player = player_cards[roundWinner(playedCards, game)]
            game.order = ordre(game.players.index(player), len(game.players))

    WINNER = max(game.players, key=get_score)
    GameOver(WINNER)

if __name__ == "__main__":
    main()