from person import Persona
#on va voir comme cette classe vas heriter les attribus et les methodes de la clase Persona

#syntax pour un objet est de la classe 

class Stundent(Persona):
    '''
    
    '''
    ''' Test
    def inheritanceTest(self):
        #check pour voir si on a heriterles attribus de Persona
        self.name
        self.last_name
        self.age

        #check pour voir si on a heriter des methodes de Persona
        self.get_Name
        self.get_Last_name
        self.get_Age

    '''
    #initialisation d un objet de la classe Studente
    def __init__(self, name:str, last_name:str, age:int, matricola:str):
        super().__init__(name,last_name,age)
        #initialisation de la classe Studente
        #instruction qui initialise un studente
        self.set_Matricola(matricola)

    #methode setter
    def set_Matricola(self, matricola:str)-> None:
        if matricola:
            self.matricola = matricola

        else:
            print("Errore! La matricola non può essere una stringa vuota")

    def get_Matricola(self) ->str:
        return self.matricola
    #methode qui nous permet de visualiser les info relatives a un objet della classe Studente
    
    def __str__(self) -> str:
        return f"\nNome: {self.get_Name()}\nCognome: {self.get_Last_name()}\nMatricola: {self.get_Matricola()}"
    
    def get_MediaEsami(self, voti_esami:list[int])->float:
        if voti_esami:
            sum:int = 0
            for voto in voti_esami:
                sum+=voto
            return round(sum/len(voti_esami),2)
        else:
            return 0.00

        #metodo che consente di fonfrontare due oggetti della classe Studente e stabilire se questi due oggetti siano uguali o meno
    def __eq__(self, other) -> bool:
        #se other è None, oppure se non è un instanza della classe Studente ritorno False
        if other is None or not isinstance(other, type(self)):
            return False
        #altrimneti valuta la seguente uguaglianza
        else:
            return self.get_Matricola() == other.get_Matricola()
    


