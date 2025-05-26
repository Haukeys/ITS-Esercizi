from abc import ABC, abstractmethod

#abc=abstract base class

class Formagenerica(ABC):

    #decorator => pour rendre la methode abstrait
    @abstractmethod
    def draw(self) -> None:
        pass

    def setShape(self, shape:str)->None:
        if shape:
            self.shape = shape

        else:
            print("Errore! la shape non può essere una stringa vuota")

    
    def getShape(self) -> str:
        return self.shape