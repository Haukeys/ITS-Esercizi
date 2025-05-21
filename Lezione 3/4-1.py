pizzas = ["margheritta","capriciosa","marinara"]

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"\nI like {pizza} pizza\n")

print(f"I like {pizza}, a lot")
#mario kart
n:int = int(input("Insert finishing Position: "))

match n:
# n=1
    case 1:
        print(f"{n}st!")
# n=2
    case 2:
        print(f"{n}nd!")
# n=3
    case 3:
        print(f"{n}rd!")
#n=+inf
    case _:
        print(f"{n}th!")