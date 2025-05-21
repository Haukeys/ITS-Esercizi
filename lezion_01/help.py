text:str=(input("inserci una frase:"))

text: str=text.title()

parole: list[str] = text.split()


result: list[str] = []                    #liste vide qui nous sera utile pour inserer les modifications que l on va apporter aux element de parole qui sont parola(qui est composer de plusieurs lettere que l on vas compter avec l indexisation)

for parola in parole:                    
    parole_inniziale = parola [:-1]
    parola_ultima = parola [-1]

    nuova = parole_inniziale + parola_ultima.upper()
    result.append(nuova)

print(" ".join(result))
#p[:-1] les : represente le debut et le -1 represente la fin.

dict[help]