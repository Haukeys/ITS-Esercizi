class Persona:
    #construtore 
    def __init__(self, name:str, last_name:str, age:int):
        self.name = name
        self.last_name = last_name
        self.age = age

    #funzione che mi mostri in output i dati relativi ad una persona
    def diaplayData(self) -> None: #ici la fleche avec le none montre le type de la valeur du return, self suffit car les parametre utiliser sont ceux de la classe persona
        print(f"Nome: {self.name}\nCognome: {self.last_name}\nEta: {self.age}")
