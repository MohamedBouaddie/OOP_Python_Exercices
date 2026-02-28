def moyenne(tab):
    if len(tab) == 0:
        return None
    return sum(tab) / len(tab)

print("moyenne [10,20,30] =", moyenne([10, 20, 30]))
print("moyenne [] =", moyenne([]))
