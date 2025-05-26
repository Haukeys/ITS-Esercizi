from typing import Self, Any
import re

class Codice_v:
#tipo di dato specializzato per il codice del volo

    def __new__(cls, v:Self|str)->Self:
        if not re.fullmatch(r'^[A-Z]{2}\d{1,4}$', v.upper().strip()):
            raise ValueError(f"la stringa {v}non rispetta lo standard per i codici dei voli")
        return super().__new__(cls, v.upper().strip())
    
from datetime import timedelta
#tipo di dato specializzato per la durata
class TimeRange:

    def __new__(cls, v:Self)->Self:
        pass




#inizzializiamo un pggetto della classe volo
class Volo:
    def __init__(self, codice:Codice_v, durata:TimeRange)->None:
        self.codice=codice
        self.durata=durata
        
    def Codice(self, codice:Codice_v)->Codice_v:
        return codice
    
    def Durata(self, durata:TimeRange)->TimeRange:
        return durata