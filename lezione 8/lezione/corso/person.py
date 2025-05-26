class Persona:
    from typing import Any
    '''
    self.name:str(attributo di tipo stringa)
    self.last_name:str(attributo di tipo stringa)
    self.age:int(attributo di tipo int)
    '''
    #inizializzare un oggetto della classe Persona
    def __init__(self, name:str, last_name:str, age:int):

        self.set_Name(name)
        self.set_Last_name(last_name)
        self.set_Age(age)

    def __str__(self):
        return f"Name: {self.name}\nLast_name: {self.last_name}\nAge: {self.age}"
    
    def set_Name(self, name:str)->None:
        self.name=name
    
    def set_Last_name(self, last_name:str)->None:
        self.last_name=last_name

    def set_Age(self, age:int)->None:
        if age < 0 or age >130:
            self.age = 0
        else:
            self.age = age
        self.age=age

    def get_Name(self)->str:
        return self.name
    
    def get_Last_name(self)->str:
        return self.last_name

    def get_Age(self)->str:
        return self.age
    
