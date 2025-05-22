#inizializzare un oggetto della classe Nazione

class Nazione:

    def __init__(self, nome:str):
        self.setNome(nome)

    def __str__(self):
        return f"Nome della Nazione:{self.nome}"
    
    def setNome(self, nome:str)->None:
        self.nome=nome
        if not isinstance(nome,str):
            raise ValueError("Il nome è già esistente")
        else:
            print("Error! il nome della nazione non può essere una stringa vuota")

