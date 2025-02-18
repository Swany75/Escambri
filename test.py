from colorama import Fore, Style

class Carta:
    def __init__(self, family, carta, value):
        self.family = family
        self.carta = carta
        self.value = value

    def get_color(self):
        """Assigna un color segons la família de la carta."""
        colors = {
            'Oros': Fore.YELLOW,
            'Bastos': Fore.GREEN,
            'Espases': Fore.BLUE,
            'Copes': Fore.RED
        }
        return colors.get(self.family, Fore.WHITE)  # Color per defecte: blanc

    def __str__(self):
        color = self.get_color()  # Obtenim el color per la família
        return f"{color}{self.carta} de {self.family} que té un valor de: {self.value}{Style.RESET_ALL}"

# Exemple d'ús:
carta1 = Carta("Oros", "As", 11)
carta2 = Carta("Bastos", "Rei", 4)
carta3 = Carta("Espases", "Cavall", 3)
carta4 = Carta("Copes", "Sota", 2)

# Mostrem les cartes
print(carta1)
print(carta2)
print(carta3)
print(carta4)