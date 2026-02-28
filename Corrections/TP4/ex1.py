n = int(input("Donner n : "))

if n <= 0:
    print("Invalid input value!")
else:
    s = 0
    for i in range(1, 2*n, 2):
        s += i
    print(f"Somme des {n} premiers impairs = {s}")

    s_alt = 0
    signe = 1
    for i in range(1, 2*n, 2):
        s_alt += signe * i
        signe *= -1
    print(f"Somme alternée des {n} premiers impairs = {s_alt}")
