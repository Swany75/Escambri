#!/usr/bin/python

import os
import random

### CONSTANTS & VARIABLES #############################################################################

FAMILIES = ['Oros', 'Bastos', 'Espases', 'Copes']
CARTES = ['As', 'Dos', 'Tres', 'Quatre', 'Cinc', 'Sis', 'Set', 'Sota', 'Cavall', 'Rei']

### CLASSES ###########################################################################################

class Carta:
    def __init__(self, family, carta, value):
        self.family = family
        self.carta = carta
        self.value = value
        
    def __str__(self):
        return f"{self.carta} de {self.family} que te un Valor de: {self.value}"

class Player:
    def __init__(self, name):
        self.name = name
        self.cartes = []
    
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
        return self.players[0]
    
    def reparteix(self):
        for player in self.players:
            for _ in range(3):
                player.addCard(self.deck.pop(0))
        self.triumph = self.deck.pop(0)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pressToContinue():
    input("Prem Enter per continuar...")

def setPlayers(joc):
    while True:
        try:
            num_players = int(input("Introdueix el nombre de jugadors (2..4): "))
            if 2 <= num_players <= 4:
                for i in range(1, num_players + 1):
                    name = input(f"Jugador {i} escriu el teu nom: ")
                    joc.addPlayer(name)
                break
            print("Error: Introdueix un numero valid (2..4)") 
        except ValueError:
            print("Error: Introdueix un numero valid (2..4)")

    joc.createDeck()
    joc.reparteix()

def player_score(player, players):
    return -sum(carta.value for carta in player.cartes), players.index(player)

def generatePlayedCardsStr(playedCards):
    if playedCards:
        return "\n".join(
            f"║  {calcSpaces(f'{i + 1}) {carta.carta} de {carta.family}', 32)}║  {calcSpaces(str(carta.value), 5)}║"
            for i, carta in enumerate(playedCards)
        )
    else:
        return "║                                  ║       ║"

def drawBoard(game, player, playedCards):
    clear()
    played_cards_str = generatePlayedCardsStr(playedCards)
    
    print(f"""
╔══════════════════════════════════════════╗
║ Triumph: {calcSpaces(str(f"{game.triumph.carta} de {game.triumph.family}"), 32)}║
╠═══════════════╦══════════════════╦═══════╣
║ Cartes en Joc ║                  ║ Valor ║
╠═══════════════╝                  ╠═══════╣
║                                  ║       ║
{played_cards_str}
║                                  ║       ║
╠══════════════════════════════════╩═══════╣
║ Torn {calcSpaces(f'Nom de {player.name}', 36)}║
╠══════════════════════════════════╦═══════╣
║                                  ║       ║
{chr(10).join(f"║  {calcSpaces(f'{i + 1}) {carta.carta} de {carta.family}', 32)}║  {calcSpaces(str(carta.value), 5)}║" for i, carta in enumerate(player.cartes))}
║                                  ║       ║
╚══════════════════════════════════╩═══════╝
""")
    playedCard = playCard(player)
    return playedCard

def finalBoard(game, playedCards, player_cards):
    clear()
    played_cards_str = generatePlayedCardsStr(playedCards)
    
    sorted_players = sorted(game.players, key=lambda p: player_score(p, game.players))
    players_str = "\n".join(
        f"║  {calcSpaces(f'{i + 1}) {player.name}', 32)}║  {calcSpaces(str(sum(carta.value for carta in player.cartes)), 5)}║"
        for i, player in enumerate(sorted_players)
    )
    
    winning_card = roundWinner(playedCards)
    winner = player_cards[winning_card]
    print(f"El guanyador de la ronda és {winner.name} amb la carta {winning_card.carta} de {winning_card.family}")
    
    print(f"""
╔══════════════════════════════════════════╗
║ Triumph: {calcSpaces(str(f"{game.triumph.carta} de {game.triumph.family}"), 32)}║
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

def playCard(player):
    while True:
        try:
            card = int(input("Tria una carta per jugar: "))
            if 1 <= card <= len(player.cartes):
                break
            else:
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
    else:
        return text[:maxlen]
    
def roundWinner(playedCards):    
    winning_card = playedCards[0]
    for carta in playedCards:
        if carta.value > winning_card.value:
            winning_card = carta
    return winning_card

### MAIN CODE #########################################################################################

def main():
    clear()
    game = Escambri()
    
    setPlayers(game)
    player = game.startPlayer()
    
    clear()
    
    print(f"Comença el jugador {player.name}")
    pressToContinue()
    
    while any(player.cartes for player in game.players):
        
        playedCards = []
        player_cards = {}
        
        for current_player in game.players:
            if current_player.cartes:
                played_card = drawBoard(game, current_player, playedCards)
                playedCards.append(played_card)
                player_cards[played_card] = current_player
                current_player.cartes.remove(played_card)
                if game.deck:
                    current_player.cartes.append(game.deck.pop(0))
        
        finalBoard(game, playedCards, player_cards)
        
        if game.deck:
            player = game.players[(game.players.index(player) + 1) % len(game.players)]

if __name__ == "__main__":
    main()