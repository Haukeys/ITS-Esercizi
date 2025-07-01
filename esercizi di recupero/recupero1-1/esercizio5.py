#Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
# dato valore intero definito threshold


def Multiply(lista:list[int], threshold:int)->list:
    prodotto = 1
    for numero in lista:
        if numero < threshold:
            prodotto *= numero
    return prodotto

threshold = 9

numeri : list = [15,60,70,2,8,19,28,47]

print(Multiply(numeri,threshold))

