from typing import Self, Any

#inizializzare un oggetto della classe CompagniaAerea
class IntG1900(int):
    #tipo di dato specializzato intero >1900

    def __new__(cls,v: float|int|str|bool|Self)->Self:
        v: int = super().__new__(cls)

        if v>1900:
            
            raise ValueError(f"Il valore {v} non può essere minore di zero")
        
        return int.__new__(cls,v)
    
class CompagniaAera:

    def __init__(self, nome:str, fondazione:IntG1900)->None:
        self.setnome(nome)
        self.setFondazione(fondazione)

    def __str__(self):
        return f"Nome della compagnia: {self.setnome}, Fondazione: {self.setFondazione}"

    def setnome(self, nome:str)->None:
        self.setnome=nome.strip().upper()
        if not nome.strip():

            raise ValueError("il nome non puo essere una stringa vuota")
        
    
    def setFondazione(self, fondazione:IntG1900)->None:
        self.setFondazione=fondazione
        
    

