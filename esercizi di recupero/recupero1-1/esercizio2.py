#2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
# classifichi i numeri in liste separate per numeri positivi e negativi.

from typing import Union

def esercizio_2(lista: list[Union[int, float]]) -> dict:
    
    dizionario_1: dict[str, list] = {}
    
    for element in lista:
        
        if element >= 0:
            
            if "positivi" not in dizionario_1:
            
                dizionario_1["positivi"] = []
            
            dizionario_1["positivi"].append(element)
            
        else:
            
            if "negativi" not in dizionario_1:
                
                dizionario_1["negativi"] = []
                
            dizionario_1["negativi"].append(element)
            
    return dizionario_1
            
lista: list[int|float] = [-1, 2, 3, -6, 4, -12, 42]

risultato: dict = esercizio_2(lista=lista)

print(risultato)
             