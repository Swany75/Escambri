#!/usr/bin/env python3

import modules.escambri as escambri
import modules.utilitats as utilitats
import modules.asciiart as asciiart

### FUNCTIONS #########################################################################################

def get_score(player):
    return player.puntuacio

### MAIN CODE #########################################################################################

def main():
    
    utilitats.clear()
    joc = escambri.Escambri()
    WINNER = None

    escambri.setPlayers(joc)
    player = joc.startPlayer()

    utilitats.clear()
    print(f"Comença el jugador {player.name}")
    utilitats.pressToContinue()

    while any(player.cartes for player in joc.players):
        playedCards = []
        player_cards = {}
        
        # Comprovar si queda només una carta a la mà de cada jugador
        if all(len(player.cartes) == 1 for player in joc.players):
            for player in joc.players:
                played_card = player.cartes.pop(0)
                playedCards.append(played_card)
                player_cards[played_card] = player
            escambri.finalBoard(joc, playedCards, player_cards)
            break

        for player_index in joc.order:
            current_player = joc.players[player_index]
            
            if current_player.cartes:
                played_card = escambri.drawBoard(joc, current_player, playedCards)
                playedCards.append(played_card)
                player_cards[played_card] = current_player
                current_player.cartes.remove(played_card)
            
                if joc.deck:
                    current_player.cartes.append(joc.deck.pop(0))

        escambri.finalBoard(joc, playedCards, player_cards)

        if joc.deck:
            player = player_cards[escambri.roundWinner(playedCards, joc)]
            joc.order = escambri.ordre(joc.players.index(player), len(joc.players))

    WINNER = max(joc.players, key=get_score)
    asciiart.gameOver(WINNER)
    
if __name__ == "__main__":
    main()