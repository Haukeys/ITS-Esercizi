#inizializzare un oggetto della classe Regione

class Regione:


    def __init__(self, nome:str):
        self.setNome(nome)

    def __str__(self):
        return f"Nome della Regione:{self.nome}"
    
    def setNome(self, nome:str)->None:
        self.nome=nome
        if not isinstance(nome,str):
            raise ValueError("Il nome è già esistente")
        else:
            print("Error! il nome della non può essere una stringa vuota")

