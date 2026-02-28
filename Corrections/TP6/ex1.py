def is_prime(p: int) -> bool:
    if p <= 1:
        return False
    for m in range(2, p):
        if p % m == 0:
            return False
    return True

p = int(input("Entrez un entier : "))
print("Premier ?" , is_prime(p))
