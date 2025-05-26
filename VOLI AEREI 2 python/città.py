from typing import Self, Any

class IntGEZ(int):

    #tipo di dato specializzato intero >=0

    def __new__(cls,v: float|int|str|bool|Self)->Self:
        v: int = super().__new__(cls)

        if v>=0:
            
            raise ValueError(f"Il valore {v} non può essere minore di zero")
        
        return int.__new__(cls,v)
    
#inizializzare un oggetto della classe Città    
class Città:

    def __init__(self, nome:str, n_abitanti:IntGEZ):
        self.Nome(nome)
        self.N_abitanti(n_abitanti)

    def Nome(self, nome:str)->str:
        
        if not nome.strip():
            raise ValueError("il nome non puo essere una stringa vuota")
        return nome
    
    def N_abitanti(self, n_abitanti:IntGEZ)->IntGEZ:
        return n_abitanti
    
    



