#inizializzare un oggetto della sotto classe rinuncica_giocatore
from partita import Partita


class Rinuncia_giocatore(Partita):
    def __init__(self, data, komi):
        super().__init__(data, komi)


#implementazione del colore del giocatore        
from enum import StrEnum, auto
class Rinunciatario(StrEnum):
    bianco=auto()
    nero=auto()