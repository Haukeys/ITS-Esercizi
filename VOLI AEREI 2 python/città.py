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
        self.setnome(nome)
        self.setn_abitanti(n_abitanti)
    
    def __str__(self):
        return f"Nome città: {self.nome}, Numero abitanti: {self.n_abitanti}"
    
    def setnome(self,nome:str)->None:
        self.nome=nome

    
    def setn_abitanti(self, n_abitanti:IntGEZ)->None:
        self.n_abitanti=n_abitanti
        if self.n_abitanti is not IntGEZ:
            raise ValueError(f"Errore , il valore deve essere maggiore o uguale di 0")
    

    
ci:Città=Città("ariccia",1)

print(ci)