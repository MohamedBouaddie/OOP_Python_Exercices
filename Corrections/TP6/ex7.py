def moyenne(tab):
    if len(tab) == 0:
        return None
    return sum(tab) / len(tab)

tab = []
while True:
    n = int(input("Entrez un entier entre 0 et 20 : "))
    if n < 0 or n > 20:
        break
    tab.append(n)

print("Tableau =", tab)
print("Moyenne =", moyenne(tab))
