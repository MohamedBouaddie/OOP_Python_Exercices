n = int(input("Donner n : "))

if n == 0:
    pass
elif n > 0:
    for x in range(2*n - 1, 0, -2):
        print(x, end=" ")
    print()
else:
    n = -n
    for x in range(1, 2*n, 2):
        print(-x, end=" ")
    print()
