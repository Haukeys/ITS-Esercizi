from person import Persona
from alieno import Alieno

#creons un objet p de la classe Persona

p:Persona = Persona("Leandro", "Pazienza", 27)

#visualisons les info de la Persona p

print(p)

#creons un objet et la classe Alieno

et:Alieno = Alieno("Andromeda")

#visualisons le info de l Alieno et

print(et)

#objet p qui invoque la methode speak()

p.speak()

#objet et qui invoque la methode speack()

et.speak()