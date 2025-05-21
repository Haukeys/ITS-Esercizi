def recursive_countdonw(n:int)->None:
    #n negativo
    if n<0:
        print("error! inserted number is negative")
    #n nullo
    elif n ==0:
        print(0)
    #n positivo
    else :
        print(n)
        recursive_countdonw(n-1)

recursive_countdonw(5)












#caso/i di arresto = element that define if, elif,else or if elif and else theme self



