#inizializzare un oggetto della classe luogo

class Luogo:
    def __init__(self, via:str, civico:str, cap:str):
        self.setVia(via)
        self.setCivico(civico)
        self.setCap(cap)

    def __str__(self):
        return f"Via: {self.via}\nCivivo: {self.civico}\nCap: {self.cap}"
    
    def setVia(self, via:str)->None:

        if via:
            self.via=via
        else:
            print("Error! La via non può essere una stringa vuota")
    
    def setCivico(self, civico:str)->None:

        if civico:
            self.civico=civico
        else:
            print("Error! il civico non può essere una stringa vuota")

    def setCap(self, cap:str)->None:

        if cap:
            self.cap=cap
        else:
            print("Error! il cap non può essere una stringa vuota")
    
    def getVia(self, via:str)->str:
        return self.via
    
    def getCivico(self, civico:str)->str:
        return self.civico
    
    def getCap(self, cap:str)->str:
        return self.cap