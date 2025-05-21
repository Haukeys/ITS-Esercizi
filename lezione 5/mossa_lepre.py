import random

def mossa_lepre(pos_lepre:int) -> int:
    pos_lepre = 0
    i=random.randint(1,10)

    match i:
        case i if 1 <= i <= 2 :
            pos_lepre += 0
            return max(1,pos_lepre)
        case i if 3 <= i <= 4:
            pos_lepre += 9
            return max(1,pos_lepre)
        case i if 5:
            pos_lepre += 12
            return max(1,pos_lepre)
        case i if 6 <= i <= 8:
            pos_lepre += 1
            return max(1,pos_lepre)
        case _:
            pos_lepre -=2
            return max(1,pos_lepre)

