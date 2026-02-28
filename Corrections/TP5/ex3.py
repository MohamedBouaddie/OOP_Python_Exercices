tab = [32, 5, 12, 8, 3, 75, 2]

i = 0
mmax = tab[0]
while i < len(tab):
    if tab[i] > mmax:
        mmax = tab[i]
    i += 1

print("Max (while) =", mmax)
print("Max (max)   =", max(tab))

mmin = tab[0]
for x in tab:
    if x < mmin:
        mmin = x

print("Min (for) =", mmin)
print("Min (min) =", min(tab))
