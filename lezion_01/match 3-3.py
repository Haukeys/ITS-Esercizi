#Esercizio 3C-3. Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
#Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

#- ["penna", "matita", "quaderno"] → "Materiale scolastico"
#- ["pane", "latte", "uova"] → "Prodotti alimentari"
#- ["sedia", "tavolo", "armadio"] → "Mobili"
#- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
#- Qualsiasi altra lista → "Categoria sconosciuta"

#Expected Output:

#['casa', 'hotel', 'b&b']
#Categoria sconosciuta

#--------------------------

#['penna', 'matita', 'quaderno']
#Materiale scolastico

#check scrren car la liste est ordonner, donc si on ne fait pas l enchainnement d insersion dans l ordre precis on obtien une erreur , 
# utiliser soit un set soit un dictionnaire . pour le dictionnaire on peut utiliser une valeur quelconque 
# pour la key ou la value. et une valeur precise pour faire un ecnhainement quelconque
oggetti: list= [] #premiere etape une lsite
for elemento in range(3): #creation d une variable qu on utilise pour compter et sauvegarder les element inseret dans la liste
    oggetto:str=input("scrivi 3 oggetto validi:") #les elements que l on va inseret
    oggetti.append(oggetto) #la function qui ajoute les elements que l on va inseret dans la liste qu on avait au debut.

match oggetti:                          #on doit comparer la liste du debut avec les liste/valeur auquel elle doit correspondre
    case oggetti if oggetto in ["penna","matita","quaderno"]: 
        print("Materiale scolastico")
        
    case oggetti if oggetto in ["pane","latte","uova"]:
         print("Prodotti alimentari")
        
    case oggetti if oggetto in ["sedia","tavolo","armadio"]:
        print("Mobili")
        
    case oggetti if oggetto in ["telefono","computer","tablet"]:
        print("Dispositivi elettronici")
        
    case _:
        print("Categoria sconosciuta")
        







