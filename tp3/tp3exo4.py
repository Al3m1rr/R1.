n = int(input("Donnez un entier n : "))
choix = input("Choisissez le type de boucle (for ou while) : ")

if choix == "for":
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        print("Iteration", i, ": factorielle =", fact)
    print("La factorielle de", n, "est", fact)

elif choix == "while":
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        print("Iteration", i, ": factorielle =", fact)
        i += 1
    print("La factorielle de", n, "est", fact)

else:
    print("Choix non valide")

