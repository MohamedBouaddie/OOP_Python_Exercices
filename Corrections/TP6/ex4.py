def affiche_liste(tab):
    print("Sans boucle :", tab)

    print("\nAvec for :")
    for x in tab:
        print(x)

    print("\nAvec while :")
    i = 0
    while i < len(tab):
        print(tab[i])
        i += 1

    print("\nAvec for + range :")
    for i in range(len(tab)):
        print(tab[i])

    print("\nAvec enumerate :")
    for i, x in enumerate(tab):
        print(f"Indice {i} : {x}")

t = [10, 20, 30, 40, 50]
affiche_liste(t)
