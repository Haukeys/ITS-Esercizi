#implementazione del colore del giocatore        
from enum import StrEnum, auto
class RegoleConteggio(StrEnum):
    giapponesi=auto()
    cinesi=auto()

from datetime import date

#inizializzare un oggetto della classe Partita

class Partita:

    def __init__(self, data:date, komi:float, regole:RegoleConteggio):
        self.setData(data)
        self.setKomi(komi)
        self.setRegole(regole)
    def __str__(self):
        return f"Data della partita: {self.data}n\Komi: {self.komi}n\Regole: {self.regole}."

    def setData(self, data:date)->None:
        self.data=data

    def setKomi(self,komi:float)->None:
        
        if komi > 0 or komi < 10:
            raise ValueError("Komi deve essere un valore decimale tra 0 e 10 inclusi")
        self.komi=komi

    def setRegole(self,regole:RegoleConteggio)->None:
        
        if not isinstance(regole,RegoleConteggio):
            raise ValueError("Komi deve essere un valore decimale tra 0 e 10 inclusi")
        self.regole=regole

