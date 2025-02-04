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
        self.triumph = self.deck.pop()

    def checkValue(self, carta):
        valors = {'As': 11, 'Tres': 10, 'Rei': 4, 'Cavall': 3, 'Sota': 2}
        return valors.get(carta, 0)

    def addPlayer(self, name):
        player = Player(name)
        self.players.append(player)
        
    def reparteix(self):
        for player in self.players:
            for _ in range(3):
                carta = self.deck.pop(0)
                player.addCard(carta)

    def startPlayer(self):
        return random.choice(self.players)
    
    def showDeck(self):
        print("DECK:")
        for carta in self.deck:
            print(f"{carta}")

### FUNCTIONS #########################################################################################

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
  
def pressToContinue():
    input("\nPulsa per continuar >>> ")
    clear()
    
def setPlayers(joc):
    while True:
        try:
            num = int(input("Introdueix el numero de jugadors: "))
            if 1 <= num <= 4:
                for i in range(1, num + 1):
                    name = input(f"Jugador {i} escriu el teu nom: ")
                    joc.addPlayer(name)
                break
            print("Error: Introdueix un numero valid (1..4)") 
        except ValueError:
            print("Error: Introdueix un numero valid (1..4)")

    joc.createDeck()
    joc.reparteix()

def drawBoard(game, player, playedCards):
    clear()
    print(f"""
╔══════════════════════════════════════════╗
║ Triumph: {calcSpaces(str(f"{game.triumph.carta} de {game.triumph.family}"), 32)}║
╠═══════════════╦══════════════════╦═══════╣
║ Cartes en Joc ║                  ║ Valor ║
╠═══════════════╝                  ╠═══════╣
║                                  ║       ║
{chr(10).join(f"║  {calcSpaces(f'{i + 1}) {carta.carta} de {carta.family}', 32)}║  {calcSpaces(str(carta.value), 5)}║" for i, carta in enumerate(playedCards))}
║                                  ║       ║
╠══════════════════════════════════╩═══════╣
║ Torn de {calcSpaces(player.name, 33)}║
╠══════════════════════════════════╦═══════╣
║                                  ║       ║
{chr(10).join(f"║  {calcSpaces(f'{i + 1}) {carta.carta} de {carta.family}', 32)}║  {calcSpaces(str(carta.value), 5)}║" for i, carta in enumerate(player.cartes))}
║                                  ║       ║
╚══════════════════════════════════╩═══════╝
""")
    
    playedCard = playCard(player)
    player.cartes.remove(playedCard)
    player.cartes.append(game.deck.pop(0)) 
    return playedCard

def playCard(player):
    while True:
        try:
            card = int(input("Tria una carta per jugar: "))
            if card >= 1 and card <= 3:
                break
            else:
                print("Error: Introdueix un numero valid (1..3)")
        except ValueError:
            print("Error: Introdueix un numero valid (1..3)")

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
    
### MAIN CODE #########################################################################################

def main():
    clear()
    game = Escambri()
    
    setPlayers(game)
    player = game.startPlayer()
    
    clear()
    
    print(f"Comença el jugador {player.name}")
    pressToContinue()
    
    while game.deck and any(player.cartes for player in game.players):
        
        playedCards = []
        
        for current_player in game.players:
            playedCards.append(drawBoard(game, current_player, playedCards))
            
        if game.deck:
            player = game.players[(game.players.index(player) + 1) % len(game.players)]

if __name__ == "__main__": 
    main()