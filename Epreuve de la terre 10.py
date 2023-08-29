base = float(input("Entrez la base : "))
exposant = int(input("Entrez l'exposant (doit être positif) : "))
while exposant < 0:
    print("L'exposant ne peut pas être négatif. Réessayez.")
    exposant = int(input("Entrez l'exposant (doit être positif) : "))
resultat = base ** exposant
print(resultat)