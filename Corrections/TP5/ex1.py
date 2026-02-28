jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

print("Liste complète :", jours)
print("Premier :", jours[0])
print("Dernier :", jours[-1])

print("\n--- Avec while ---")
i = 0
while i < len(jours):
    print(i, ":", jours[i])
    i += 1

print("\n--- Avec for + range ---")
for i in range(len(jours)):
    print(i, ":", jours[i])

print("\n--- Ordre inverse (Dimanche -> Lundi) ---")
for j in jours[::-1]:
    print(j)

print("\n--- For-each ---")
for j in jours:
    print(j)

print("\n--- enumerate ---")
for i, j in enumerate(jours):
    print(i, ":", j)
