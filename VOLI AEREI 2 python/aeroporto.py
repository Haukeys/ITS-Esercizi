#inizzializare un oggeto della classe aeroporto
   
class Aeroporto:
    
    def __init__(self, nome:str, codice:str)->None:
        self.setnome(nome)
        self.setcodice(codice)

    def __str__(self):
        return f"Nome del aeroporto: {self.nome}, Codice: {self.codice}"
    
    def setnome(self, nome:str)->str:

        self.nome=nome.strip().upper()

        if not nome.strip():

            raise ValueError("il nome non puo essere una stringa vuota")

    
    def setcodice(self, codice:str)->None:

        self.codice = codice.strip().upper()

        if len(codice) !=4 or not codice.isalpha():

            raise ValueError("Il codice non rispetta lo standard ICAO")
        
if __name__=="__main__":
    aer:Aeroporto=Aeroporto("leonardo davinci", "lifm")   
print(aer)

    
