'''#dal file personapy importa Persona
from persona import Persona

#creo una persona(creation d un objet/instance de la classe personne)
fn:Persona = Persona("Leandro", "Pazienza", 27)

print(fn.last_name,fn.name,fn.age)
#si on utilise l expression print(fn) on voit dans le terminal l addresse de memoire de la fonction

# richiamare la funzione displayData della classe Persona per mostrare in output i dati relativi alla personna fn
fn.diaplayData()

''' 
#dal file persona2 importa la classe Persona
from persona2 import Persona

fn:Persona = Persona() #objet vide Persona()

#richiamo la funzione displayData della classe Persona per mostrare in output le informazione relative all'oggette fn
fn.diaplayData()

#modifica il nome della persona fn
fn.setName("Leandro")

print("------------------")

fn.diaplayData()
#modificare il cognome della persona fn
fn.setLastname("Pazienza")

#modifica l eta della persona fn
fn.setAge(29)

print("------------------")

fn.diaplayData()
print("------------------")

print(fn.getName(), fn.getLastName(), fn.getAge())


