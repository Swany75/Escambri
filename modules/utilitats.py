#!/usr/bin/env python3

import os

### FUNCIONS GENERALS #################################################################################

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pressToContinue():
    input("\nPulsa per continuar >>>")