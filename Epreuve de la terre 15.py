def valeur_milieu(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    return c

a = int(input("Entrez le premier entier : "))
b = int(input("Entrez le deuxième entier : "))
c = int(input("Entrez le troisième entier : "))

milieu = valeur_milieu(a, b, c)
print(milieu)