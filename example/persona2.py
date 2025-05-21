class Persona:
    def __init__(self): #self fonction base/qui contien le parametre de la classe Persona
        self.name =""
        self.last_name = ""
        self.age = int = 0

    #funzione che mi mostri in output i dati relativi ad una persona
    def diaplayData(self) -> None: #ici la fleche avec le none montre le type de la valeur du return, self suffit car les parametre utiliser sont ceux de la classe persona
        print(f"Nome: {self.name}\nCognome: {self.last_name}\nEta: {self.age}")

#ici on utilise la methode set pour modifier les valeur qu on a preset dans le construteur de la fonction ( appeler attribu de classe)

    #funzione che mi consenta di modificare il valore di self.name
    def setName(self, name:str) ->None:# none car la fonction ne "return" rien
        self.name = name

    #funzione che mi consenta di impostare il valore self.last_name
    def setLastname(self, last_name:str) ->None:
        self.last_name = last_name

    #funzione che mi consenta di impostare il valore self.age
    def setAge(self, age:int) -> None:
        if age < 0 or age >130:
            self.age = 0
        else:
            self.age = age
    
#ici on utilise le methode get pour "return" la valeur donc on ne met plus fleche none mais on precise les types de maniere correcte

    #funzione che mi consenta di ritornare il valore di self.name
    def getName(self) ->str:
        return self.name
    
    #funzione che mi consenta di ritornare il valore di self.last_name
    def getLastName(self) -> str:
        return self.last_name
    
    #funzione che mi consenta di ritornare il valore di self.age
    def getAge(self) -> int:
        return self.age
    
