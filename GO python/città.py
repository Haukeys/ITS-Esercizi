#inizializzare un oggetto della classe Città

class Città:

    def __init__(self, nome:str):
        self.setNome(nome)

    def __str__(self):
        return f"Nome della Città:{self.nome}"
    
    def setNome(self, nome:str)->None:
        self.nome=nome
        if not isinstance(nome,str):
            raise ValueError("Il nome è già esistente")
        else:
            print("Error! il nome della città non può essere una stringa vuota")

