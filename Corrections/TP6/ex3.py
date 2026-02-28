def puissancePos(x: float, n: int) -> float:
    if n <= 0:
        return 0
    r = 1.0
    for _ in range(n):
        r *= x
    return r

def puissance(x: float, n: int) -> float:
    if n > 0:
        return puissancePos(x, n)
    elif n < 0:
        return 1.0 / puissancePos(x, -n)
    else:
        return 1.0

x = float(input("Entrez x : "))
n = int(input("Entrez n : "))
print("x^n =", puissance(x, n))
