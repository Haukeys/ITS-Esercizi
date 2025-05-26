class Persona:
    '''
    self.name:str(attributo di tipo stringa)
    self.last_name:str(attributo di tipo stringa)
    self.age:int(attributo di tipo int)
    '''
    #inizializzare un oggetto della classe Persona
    def __init__(self):

        self.set_Name=""
        self.set_Last_name=""
        self.set_Age=int=0

    def __str__(self):
        return f"Name: {self.name}\nLast_name: {self.last_name}\nAge: {self.age}"
    
    #funzione che mi consente di impostare il valore di self.name
    def set_Name(self, name:str)->None:
        if name:
            self.name=name
        else:
            print("Error! il nome non può essere una stringa vuota")

    def set_Last_name(self, last_name:str)->None:
        if last_name:
            self.last_name=last_name
        else:
            print("Error! il cognome non può essere una stringa vuota")

    def set_Age(self, age:int)->None:
        if age < 0 or age >130:
            self.age = 0
        else:
            self.age = age
        self.age=age

    def get_Name(self, name:str)->str:
        return self.name
    
    def get_Last_name(self, last_name:str)->str:
        return self.last_name

    def get_Age(self, age:int)->str:
        return self.age