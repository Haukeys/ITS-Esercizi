from person import Persona
from studente import Stundent

#creon un objet p de la classe Persona
p:Persona = Persona("Leandro","Pazienza",27)

#visualisation des info relatives alla personne p
print(p)


print("-----------------------------------------------------")

#creon un objet studente1 de la classe Studente
studente1: Stundent = Stundent("Cyril","Gane",46,"56448481")

print(studente1)

#je dois controler que studente1 est instance de la clasee Studente
if isinstance(studente1,Stundent):
    print("\nstudent11 è un oggetto della classe Studente")

#la fonction isinstance (obj,Class)->True si l objet è instance de la classe Studente herite de la classe Persona
if isinstance(studente1,Persona):
    print("\nl'oggetto studente1 è anche un instanza della classe Persona")
else:
    print("\nl'oggetto studente1 è solo un instanza della classe Studente e non della classe Persona")

#on doit controler que l objet p est une instance de la classe Studente
if isinstance(p, Stundent):
    print("\n l'oggetto p èistanza della classe Persona ed è anche istanza della classe Studente")
else:
    print("\n l' oggetto p è solo istanza della classe Persona ma non è istanza della classe Studente")

#on veux controler si Studente est la sous classe de la classe Persona
#issubclass(Class1,Class2) -> controllare se Classi1 sottoclasse della Classe2 ->in caso affermattivo ritorna True
if issubclass(Stundent,Persona):
    print("\n la classe Studente è una sotto classe di Persona")

print(studente1)
print("-----------------------------------------------------------")
print(p)
print("-----------------------------------------------------------")



print(f"\n la media dei voti relativi agli esami sostenuti dallo studente1 è:{studente1.get_MediaEsami([10,20,30])}")

studente2:Stundent = Stundent(p.get_Name(), p.get_Last_name(), p.get_Age(),  "0987654")
print(studente2)

#confrontare se studente1 == p
print("\n", studente1 == p)

#confrontare se studente1 == studente2
print("\n",studente1 == studente2)

#modificare nome , cognome , età dello studente2 affinchè abbia stesso nome ,cognome , età dello studente1
studente2.set_Name(studente1.get_Name())
studente2.set_Last_name(studente1.get_Last_name())
studente2.set_Age(studente1.get_Age())

print("\n", studente1 == studente2)

#ho forzato la matricola dello 

#
studente2.set_Matricola(studente1.get_Matricola())

print("\n", studente1 == studente2)
