#inizializzare un oggetto della classe Torneo

class Torneo:

    def __init__(self, nome:str, descrizione:str, edizione:int):
        
        self.setNome(nome)
        self.setDescrizione(descrizione)
        self.setEdizione(edizione)

    def __str__(self):
        return f"Nome: {self.nome}\nDescrizione: {self.descrizione}\nedizione: {self.edizione}"

    def setNome(self, nome:str)->None:
        if nome:
            self.nome=nome
        
        else:
            print("Error! il nome non può essere una stringa vuota")
    
    def setDescrizione(self, descrizione:str)->None:
        if descrizione:
            self.descrizione=descrizione
        
        else:
            print("Error! La descrizione non può essere una stringa vuota")

    def setEdizione(self, edizione:int)->None:
        if edizione:
            self.edizione=edizione
        
        else:
            print("Error! L'edizione non può essere un valore vuoto")






    