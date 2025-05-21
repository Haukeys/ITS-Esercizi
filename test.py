result = []
for x in range(1, 4):
    inner_list = []
    for y in range(1, 4):
        inner_list.append(x * y)
    result.append(inner_list)

print(inner_list)
print(result)