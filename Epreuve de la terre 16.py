entrees = input("Entrez une liste d'entiers séparés par des espaces : ")
liste_entiers = entrees.split()

try:
    liste_entiers = [int(x) for x in liste_entiers]
    if liste_entiers == sorted(liste_entiers):
        print("Triée !")
    else:
        print("Pas triée !")
except ValueError:
    print("Erreur")