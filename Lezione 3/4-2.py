animals:list[str]=["dog","wolf","cat"]

for item in animals:
    print(item)


for item in animals:
    print(f"{item}would make a great pet")

print(f"{','.join(animals)} all have 4 legs. ANy of these animals would make a great pet" )
