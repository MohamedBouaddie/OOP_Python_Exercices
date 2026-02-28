t = [10, 20, 30, 40, 50]
print("Originale :", t)

t1 = t.copy()
t1.reverse()
print("reverse() :", t1)

print("slicing   :", t[::-1])
print("reversed  :", list(reversed(t)))

t4 = []
for i in range(len(t)-1, -1, -1):
    t4.append(t[i])
print("boucle for:", t4)
