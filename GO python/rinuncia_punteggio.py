#inizializzare un oggetto della classe Rinuncia_punteggio
from partita import Partita

class Rinuncia_punteggio(Partita):
    
    def __init__(self, data, komi, punteggio_bianco:int, punteggio_nero:int):
        super().__init__(data, komi)
        #inizializzare la classe Rinuncia_Punteggio
        #instruzione che inizializa una Rinuncia_punteggio
        self.setPunteggioBianco(punteggio_bianco)
        self.setPunteggioNero(punteggio_nero)

    def __str__(self):
        return f"Data della partita: {self.data}n\Komi: {self.komi}n\Punteggio Bianco{self.puntenggio_bianco}n\Punteggio Nero{self.puntenggio_nero}."

    def setPunteggioBianco(self, punteggio_bianco:int)-> None:
        if punteggio_bianco >0:
            self.puntenggio_bianco=punteggio_bianco
        else:
            print("Error! il punteggio bianco non può essere 0 o negativo")
 
    def setPunteggioNero(self,punteggio_nero:int)->None:
        if punteggio_nero > 0:
            self.puntenggio_nero=punteggio_nero
        else:
            print("Error! il punteggio nero non può essere 0 o negativo")
    
    def getPunteggioBianco(self,punteggio_bianco:int)->int:
        return punteggio_bianco
    
    def getPunteggioNero(self,punteggio_nero:int)->int:
        return punteggio_nero
    