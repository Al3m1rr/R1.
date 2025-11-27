nMax = 3

v1 = []
v2 = []

print("Quelle est la taille de vos vecteurs [entre 1 et", nMax, "] ?")
n = int(input())

while n < 1 or n > nMax:
    print("Veuillez entrer une valeur entre 1 et", nMax, ":")
    n = int(input())

print("Saisie du premier vecteur :")
for i in range(n):
    print("v1[", i, "] =")
    val = int(input())
    v1.append(val)


print("Saisie du second vecteur :")
for i in range(n):
    print("v2[", i, "] =")
    val = int(input())
    v2.append(val)

produit_scalaire = 0
for i in range(n):
    produit_scalaire += v1[i] * v2[i]

print("Le produit scalaire de v1 par v2 vaut", float(produit_scalaire), ".")





