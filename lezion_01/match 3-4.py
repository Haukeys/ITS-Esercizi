animale:list[str]=[]

for item in range(1):
    nome_animale:str=input("Inserici il nome di un animale")
    animale.append(nome_animale)

    match animale:
        case animale if nome_animale in ["cane","gatto","cavallo","elefante","leone"]:
            print(f"{nome_animale} appartiene alla categoria dei Mammiferi!")
        
        case animale if nome_animale in ["serpente","lucertola","tartaruga","coccodrillo"]:
            print(f"{nome_animale} appartiene alla categoria dei Rettili!")
        
        case animale if nome_animale in ["aquila","pappagallo","gufo","falco"]:
            print(f"{nome_animale} appartiene alla categoria degli Uccelli!")
        
        case animale if nome_animale in ["squalo","trota","salmone","carpa"]:
            print(f"{nome_animale} appartiene alla categoria dei Pesci!")

        case _:
            print(f"Non so dire in quale categoria classificare l'animale {nome_animale}")


