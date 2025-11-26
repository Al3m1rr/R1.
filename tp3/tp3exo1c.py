

nb_inf = 0
nb_sup10 = 0
nb_sup15 = 0


for i in range(10):
    nb_donnee = int(input("Saisir une valeur : "))
    if (nb_donnee) > 20 or (nb_donnee < 0) :
        nb_donnee = int(input("Saisir une valeur : "))
        if nb_donnee < 10 :
            nb_inf += 1

        if 10 <= nb_donnee < 15 :
            nb_sup10+=1

        if nb_donnee >= 15 :
            nb_sup15+=1
    else :
        if nb_donnee < 10 :
            nb_inf += 1

        if 10 <= nb_donnee < 15 :
            nb_sup10+=1

        if nb_donnee >= 15 :
            nb_sup15+=1

print(nb_inf,nb_sup10,nb_sup15)




