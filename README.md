## Escambri

El joc de l'Escambri (Brisca) fet amb Python

```python
╔══════════════════════════════════════════╗
║ Triumph: Tres de Copes                   ║
╠═══════════════╦══════════════════╦═══════╣
║ Cartes en Joc ║                  ║ Valor ║
╠═══════════════╝                  ╠═══════╣
║                                  ║       ║
║                                  ║       ║
╠══════════════════════════════════╩═══════╣
║ Torn de {calcSpaces(player.name, 33)}║
╠══════════════════════════════════╦═══════╣
║                                  ║       ║
{chr(10).join(f"║  {calcSpaces(f'{i + 1}) {carta.carta} de {carta.family}', 32)}║  {calcSpaces(str(carta.value), 5)}║" for i, carta in enumerate(player.cartes))}
║                                  ║       ║
╚══════════════════════════════════╩═══════╝
```