x=int
y=int

point= (x, y) = x(input("inserici x:")), y(input("inserici y:"))

match point:
    case (0, 0):
        print("Il punto si trova nell'origine.")
    
    case (x, 0):
        print("Il punto sta sull'asse X.")

    case (0, y):
        print("Il punto si trova sull'asse Y")

    case point if x > 0 and y > 0:
        print("Il punto si trova nel primo quadrante")

    case point if x < 0 and y > 0:
        print("Il punto si trova nel secondo quandrante")
    
    case point if x < 0 and y < 0:
        print("Il punto si trova nel terzo quadrante.")

    case _:
        print("Il punto si trova nel quarto quadrante")
    
