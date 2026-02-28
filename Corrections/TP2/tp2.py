i1 = 0
pi = 0.0
b = True

print("=== Ex 1 ===")
print("i1 =", i1, "| type =", type(i1))
print("pi =", pi, "| type =", type(pi))
print("b  =", b,  "| type =", type(b))

i1 = 55
i2, i3, m = 22, 42, 77
pi = 3.14
b = False

print("\n=== Ex 2 ===")
i4 = i1
print("i4 = i1 ->", i4)
i4 = i2 + i3
print("i4 = i2 + i3 ->", i4)
i4 = i3 - i1
print("i4 = i3 - i1 ->", i4)
i4 += 6
print("i4 += 6 ->", i4)
i4 -= 3
print("i4 -= 3 ->", i4)

print("\n=== Ex 3 ===")
i4 = i3 / i2
print("i3 / i2 =", i4, type(i4))
i4 = i3 // 27
print("i3 // 27 =", i4, type(i4))
i4 = i3 % 4
print("i3 % 4 =", i4, type(i4))
i4 = i1 ** 2 * i2
print("i1 ** 2 * i2 =", i4, type(i4))

print("\n=== Ex 4 ===")
i4 = 5 * i2**2 + 17 * i2 + 88
print("i4 =", i4)

print("\n=== Ex 5 ===")
r = 1.1
surface = pi * r**2
print("Surface =", surface)
