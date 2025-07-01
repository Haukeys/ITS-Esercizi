#1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in 
#un dizionario. 
#Se la chiave è già presente, 
#somma il valore al valore già associato alla chiave.


def Convert(lista:list[tuple]) -> dict:

    dizionario1:dict={}
    # explorant la liste,
    for key,value in lista: #for tupla in lista:  * l etape si dessous et superficier donc on peut l enlever*1

        # 1*  key,value=tupla #ou  key,value=tupla[0],tupla[1] dans le cas commenter on peu voir que ici on explore les elements 0 =key et 1=value et non pas un incdice
        if key in dizionario1:

            dizionario1[key]+=value#la valeur existe deja/la valeur associer a cette key
        else:

            dizionario1[key]=value#la valeur n existe pas/la valeur associer a cette key

    return dizionario1


menu:tuple=[(0,"val1"),(1,"val2"),(2,"val3"),(3,"val4"),(2,"val3")]

print(Convert(menu))


'''
def esercizio_1(lista_1: list[tuple]) -> dict:
    
    dict_1: dict = {}
    
    for element in lista_1:
        
        key, value = element[0], element[1]
        
        if key in dict_1:
            
            dict_1[key] += value
            
        else:

            dict_1[key] = value
            
    return dict_1
'''








