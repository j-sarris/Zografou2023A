#remove duplicates from a list

list = [12, 1, 4, 12, 5, 4, 12]

uniques = []

for x in list:
    if x not in uniques:
        uniques.append(x)

print(list)
print(uniques)


