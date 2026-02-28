n = int(input("Donner n : "))
p = int(input("Donner p : "))

if n > 0 and p > 0:
    resultat = 1
    for _ in range(p):
        resultat *= n

    for i in range(p):
        print(n, end="")
        if i < p - 1:
            print(" * ", end="")
    print(" = ", resultat, sep="")
