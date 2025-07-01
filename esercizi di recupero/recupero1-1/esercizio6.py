#Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
#a) 2, 4, 6, 8, 10, 12, 14
#b) 1, 4, 7, 10, 13
#c) 30, 25, 20, 15, 10, 5, 0
#d) 5, 15, 25, 35, 45

for a in range(2, 15, 2):
    print(a ,end=", ")


for b in range(1, 14, 3):
    print(b ,end=", ")


for c in range(30, -1, -5):
    print(c ,end=", ")
   

for d in range(5, 46, 10):
    print(d ,end=", ")