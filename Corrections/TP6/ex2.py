def saisiePos() -> int:
    n = int(input("Saisir un nombre strictement positif : "))
    while n <= 0:
        n = int(input("Saisir un nombre strictement positif : "))
    return n

a = saisiePos()
b = saisiePos()
print("Somme des 2 nombres =", a + b)
