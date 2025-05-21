import random

def mossa_tartaruga(pos_tartaruga:int) -> int:
    pos_tartaruga = 0
    i=random.randint(1,10)

    match i:
        case i if 1<=i<= 5 :
            pos_tartaruga += 3
            return max(1,pos_tartaruga)
            
        case i if 6 <= i <= 7:
            pos_tartaruga -= 6
            return max(1,pos_tartaruga)
        case _:
            pos_tartaruga += 1
            return max(1,pos_tartaruga)
        
            

