from typing import Self, Any
import re

class codice_v:

    def __new__(cls, v:Self|str)->Self:
        if not re.fullmatch(r'^[A-Z]{2}\d{1,4}$', v.upper().strip()):
            raise ValueError(f"la stringa {v}non rispetta lo standard per i codici dei voli")
        return super().__new__(cls, v.upper().strip())
    
class Volo:
    
    def __init__(self, codice:codice_v)->None:
        self.codice=codice
    
    def Codice(self, codice:codice_v):
        return codice