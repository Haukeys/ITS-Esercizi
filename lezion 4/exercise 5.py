def add_one(num):
     return num += 1

def add_one_to_list(lista:list[int]):
    new_list:list=[]
    for num in new_list:
        new_list.append(add_one(num))
    print(new_list)

liste:list[int]=[1,2,3]
add_one_to_list(liste)