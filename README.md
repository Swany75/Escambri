# Escambri

El joc de l'Escambri (Brisca) fet amb Python. Aixo es un projecte fet per el mòdul d'Implantació d'aplicacions web del grau superior d'ASIX 2024-25.

![Cartes](https://cuatrola.es/wp-content/uploads/2018/04/ases-1024x256.png)

# Regles de l'Escambri

```
███████╗███████╗ ██████╗ █████╗ ███╗   ███╗██████╗ ██████╗ ██╗
██╔════╝██╔════╝██╔════╝██╔══██╗████╗ ████║██╔══██╗██╔══██╗██║
█████╗  ███████╗██║     ███████║██╔████╔██║██████╔╝██████╔╝██║
██╔══╝  ╚════██║██║     ██╔══██║██║╚██╔╝██║██╔══██╗██╔══██╗██║
███████╗███████║╚██████╗██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║██║
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝
```

## 1. Objectiu del Joc
L'objectiu del joc és guanyar el màxim de punts jugant cartes en cada ronda. Cada carta té un valor assignat, i el jugador que guanya una ronda acumula els punts corresponents a la carta jugada. El jugador amb més punts al final del joc guanya.

## 2. Mecànica del Joc
- El joc es juga entre 2 i 4 jugadors.
- Cada jugador rep 3 cartes al començament del joc.
- Hi ha un **triumph** que determina quina família és la més forta per a la ronda.
- Els jugadors juguen una carta al seu torn.
- La carta guanyadora de la ronda es determina per la seva força, ajustada pel valor de la família **triumph**. Si la carta jugada pertany a la mateixa família que el **triumph**, el seu valor es multiplica per 3.

## 3. Valor de les Cartes
Les cartes tenen els següents valors:
- **As**: 11 punts
- **Dos**: 0 punts
- **Tres**: 10 punts
- **Quatre**: 0 punts
- **Cinc**: 0 punts
- **Sis**: 0 punts
- **Set**: 0 punts
- **Sota**: 2 punts
- **Cavall**: 3 punts
- **Rei**: 4 punts

## 4. Inici del Joc
- Els jugadors es distribueixen aleatòriament i un jugador comença el joc.
- Els jugadors han de triar una carta per jugar durant el seu torn.
- El jugador que comença la ronda es tria aleatòriament.

## 5. Desenvolupament de la Ronda
- Cada jugador escull una carta de la seva mà per jugar-la.
- El guanyador de la ronda és el jugador que ha jugat la carta més alta, tenint en compte el valor i l'efecte del **triumph**.
- Els punts de la ronda es sumaran al jugador guanyador.

## 6. Final del Joc
- El joc acaba quan tots els jugadors han jugat les seves cartes.
- El jugador amb més punts guanya la partida.
- El guanyador és anunciat amb el seu nom i els punts aconseguits.

## 7. Excepcions i Errors
- Els jugadors no poden jugar una carta si no la tenen a la mà.
- Si un jugador intenta triar una carta que no té a la mà, es mostrarà un missatge d'error.
- El nombre de jugadors ha de ser entre 2 i 4.

## 8. Final de Ronda
Al final de cada ronda, es mostrarà un tauler amb les cartes jugades, els punts obtinguts i el guanyador de la ronda.

# Joc

```
╔══════════════════════════════════════════╗
║ Triumph: As de Copes                     ║
╠═══════════════╦══════════════════╦═══════╣
║ Cartes en Joc ║                  ║ Valor ║
╠═══════════════╝                  ╠═══════╣
║                                  ║       ║
║  1) Tres de Oros                 ║  10   ║
║  2) Dos de Espases               ║  0    ║
║  3) Cinc de Bastos               ║  0    ║
║                                  ║       ║
╠══════════════════════════════════╩═══════╣
║ Torn de Juan                             ║
╠══════════════════════════════════╦═══════╣
║                                  ║       ║
║  1) Cinc de Espases              ║  0    ║
║  2) Quatre de Espases            ║  0    ║
║  3) Cavall de Espases            ║  3    ║
║                                  ║       ║
╚══════════════════════════════════╩═══════╝
``` 
---
```
El guanyador de la ronda és Josep amb la carta As de Bastos
Ha guanyat 15 punts aquesta ronda.

╔══════════════════════════════════════════╗
║ Triumph: As de Copes                     ║
╠═══════════════╦══════════════════╦═══════╣
║ Cartes en Joc ║                  ║ Valor ║
╠═══════════════╝                  ╠═══════╣
║                                  ║       ║
║  1) As de Bastos                 ║  11   ║
║  2) Sis de Oros                  ║  0    ║
║  3) Rei de Bastos                ║  4    ║
║  4) Quatre de Bastos             ║  0    ║
║                                  ║       ║
╠════════════╦═════════════════════╬═══════╣
║ Torn Final ║                     ║ Punts ║
╠════════════╝                     ╠═══════╣
║                                  ║       ║
║  1) Josep                        ║  15   ║
║  2) Juan                         ║  0    ║
║  3) Diego                        ║  0    ║
║  4) Andreu                       ║  0    ║
║                                  ║       ║
╚══════════════════════════════════╩═══════╝

Final de la ronda
```

## Recursos emprats

[Text to Ascii Art](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)