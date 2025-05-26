#inizzializare un oggeto della classe aeroporto
   
class Aeroporto:
    
    def __init__(self, nome:str, codice:str)->None:
        self.nome=nome
        self.codice=codice

    def Nome(self, nome:str)->str:
        
        if not nome.strip():
            raise ValueError("il nome non puo essere una stringa vuota")
        return nome
    
    def Codice(self, codice:str)->str:
        codice = codice.strip().upper()
        if len(codice) !=4 or not codice.isalpha():
            raise ValueError("Il codice non rispetta lo standard ICAO")
        return codice
        