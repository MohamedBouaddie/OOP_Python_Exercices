import math

print("Résolution de l'équation : ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a != 0:
    delta = b**2 - 4*a*c
    print("delta =", delta)

    if delta < 0:
        print("Cette équation n'a pas de solution réelle.")
    elif delta == 0:
        x = -b / (2*a)
        print("Solution unique : x =", x)
    else:
        r = math.sqrt(delta)
        x1 = (-b - r) / (2*a)
        x2 = (-b + r) / (2*a)
        print("Deux solutions :")
        print("x1 =", x1)
        print("x2 =", x2)
else:
    if b != 0:
        x = -c / b
        print("Équation linéaire : solution x =", x)
    else:
        if c == 0:
            print("Tout réel est solution (infinité de solutions).")
        else:
            print("Aucune solution.")
