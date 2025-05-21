testa=0
croce=0
i=1
while i<=8:
    lancio:str=input(f"Inserici't'o'T'per testa o 'c'o'C'per croce lancio {i}:").lower()
    
    match lancio:

        case "t"|"T":
            testa+=1
            i+=1
        
        case "c"|"C":
            croce+=1
            i+=1

        case _:
            print("Inserire un valore valido")

percentuale_testa=(testa/8)*100
percentuale_croce=(croce/8)*100

print(f'Totale "{testa}":')
print(f'Percentuale"testa":{percentuale_testa:.2f}%')

print(f'Totale "{croce}":')
print(f'Percentuale"testa":{percentuale_croce:.2f}%')







    
