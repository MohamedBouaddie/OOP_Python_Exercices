notes = []

while True:
    x = float(input("Note (0..20) : "))
    if x < 0 or x > 20:
        break
    notes.append(x)

if len(notes) == 0:
    print("Aucune note saisie.")
else:
    print("Notes :", notes)
    print("Moyenne =", sum(notes)/len(notes))
