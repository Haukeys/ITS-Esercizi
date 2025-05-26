class Alieno:
    '''
    di un alieno ci serve sapere la galassia di provenienza
    self.galaxy:str
    '''

    #initialisation d un objet de la classe Alieno
    def __init__(self,galaxy:str):
        
        self.setGalaxy(galaxy)

    def setGalaxy(self,galaxy:str)->None:
        if galaxy:
            self.galaxy = galaxy

        else:
            print("Errore! la galassia di provennenienza non deve essere una stringa vuota")

    def getGalaxy(self) -> str:
        return self.galaxy
    
    def __str__(self)->str:
        return f"\nAlieno provveniente dalla galassia {self.getGalaxy()}\n"

    def speak(self)->None:
        print("Diooooooooooooooo the world")