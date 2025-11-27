date = input("Entrez une date au format jjmmaaaa : ")

if len(date) != 8:
    print("Erreur : la date doit contenir exactement 8 chiffres (jjmmaaaa).")
else:
    try:
        jour = int(date[0:2])
        mois = int(date[2:4])
        annee = int(date[4:8])


        if mois < 1 or mois > 12:
            print("Date invalide : le mois doit être compris entre 01 et 12.")
        else:
            if mois in [1, 3, 5, 7, 8, 10, 12]:
                max_jours = 31
            elif mois in [4, 6, 9, 11]:
                max_jours = 30
            else:
                if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
                    max_jours = 29
                else:
                    max_jours = 28

            if jour < 1 or jour > max_jours:
                print("Date invalide : le jour n'est pas correct pour ce mois et cette année.")
            else:
                print("Date correcte.")
    except ValueError:
        print("Erreur : la date doit contenir uniquement des chiffres.")
