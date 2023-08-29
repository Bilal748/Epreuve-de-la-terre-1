import math

nombre = int(input("Entrez un entier positif : "))
while nombre < 0:
    print("L'entier doit être positif. Réessayez.")
    nombre = int(input("Entrez un entier positif : "))

racine_carree = math.sqrt(nombre)
print(racine_carree)