#Esercizio 3C-1. Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.\
#Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:

#- 10 → "Eccellente"
#- 8-9 → "Molto buono"
#- 6-7 → "Sufficiente"
#- 4-5 → "Insufficiente"
#- 1-3 → "Gravemente insufficiente"
#- Altro caso → "Voto non valido"

#Expected Output:

#Inserisci il voto: 5
#Output: Insufficiente
#- - - - - - - - - - -
#Inserisci il voto: 11
#Output: Voto non valido

voto:int=int(input("inserici un voto:"))

match voto:
    case 1|2|3:
        print("Gravement insufficiente")
    
    case 4|5:
        print("Insufficiente")
    
    case 6|7:
        print("Sufficiente")
    
    case 8|9:
        print("molto buono")
    
    case 10:
        print("Ecellente")
    
    case _:
        print("Voto non valido")
    
