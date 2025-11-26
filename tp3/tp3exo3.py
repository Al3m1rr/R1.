import random


nombre_mystere = random.randint(0, 100)
compteur = 0

print("Je pense à un nombre entre 0 et 100, à vous de le deviner.")

while True:

    try:
        utilisateur = int(input("Entrez votre estimation : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue


    compteur += 1


    if utilisateur < nombre_mystere:
        print("C'est plus grand !")
    elif utilisateur > nombre_mystere:
        print("C'est plus petit !")
    else:
        print("Bravo ! Vous avez trouvé le nombre mystère",nombre_mystere," en ",compteur,"essais.")
        break


