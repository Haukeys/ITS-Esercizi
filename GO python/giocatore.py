#implementazione del colore della pietra del giocatore
from enum import StrEnum, auto

class Colore(StrEnum):
    bianco = auto()
    nero = auto()

#inizializzare un oggetto della classe Giocatore

class Giocatore:

    def __init__(self, nickname:str, nome:str, cognome:str, rank:int, colore:Colore):
        self.setNickmame(nickname)
        self.setNome(nome)
        self.setCognome(cognome)
        self.setRank(rank)
        self.setColore(colore)
    def __str__(self):
        return f"Nickname: {self.nickname}\nNome: {self.nome}\nCognome: {self.cognome}\nRank: {self.rank}n\Colore: {self.colore}"

    def setNickmame(self, nickname:str)->None:
        self.nickname=nickname
        if not isinstance(nickname,str):
            raise ValueError("Il nome è già esistente")
        else:
            print("Error! il nickname non può essere una stringa vuota")

    def setNome(self, nome:str)->None:
        if nome:
            self.nome=nome
        
        else:
            print("Error! il nome non può essere una stringa vuota")
    
    def setCognome(self, cognome:str)->None:
        if cognome:
            self.cognome=cognome
        
        else:
            print("Error! il cognome non può essere una stringa vuota")

    def setRank(self, rank:int)->None:
        if rank < 0 :
            self.rank = 1
        else:
            self.rank = rank

    def setColore(self, colore:Colore)->None:
        if not isinstance(colore,Colore):
            raise ValueError("Il colore deve essere bianco o nero")
        self.colore=colore
