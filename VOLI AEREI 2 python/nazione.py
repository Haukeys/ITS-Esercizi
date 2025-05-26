#inizializzare un oggetto della classe Nazione

class Nazione:

    def __init__(self, nome:str):
        self.Nome(nome)
    
    def Nome(self, nome:str)->None:
        
        if not nome.strip():
            raise ValueError("il nome non puo essere una stringa vuota")
        return nome
    
