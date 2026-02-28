nombres = [10, 15, 20, 25, 30, 35, 40]

pairs = []
impairs = []

for x in nombres:
    if x % 2 == 0:
        pairs.append(x)
    else:
        impairs.append(x)

print("Nombres :", nombres)
print("Pairs   :", pairs)
print("Impairs :", impairs)
