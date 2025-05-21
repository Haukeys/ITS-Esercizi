def check_each(list_of_numbers:list):

    for i in list_of_numbers:
            if i > 5:
                print(f"{i} bigger than 5")
            elif i<5:
                print(f"{i} smaller than 5")
            else :
                print(f"{i} equal 5")
        


list_of_numbers:list[int]=[1,2,3,4,5,6,7] #le cicle va implementer dans le def mais les element qui utilise le def endehord du def

check_each(list_of_numbers)