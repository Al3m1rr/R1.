nb_saisi = int(input("Saisi un nombre : "))
derniere_somme = 0
somme_total = 0

for i in range(nb_saisi):
    derniere_somme = i
    somme_total+=derniere_somme
    if (somme_total == nb_saisi) :
        break
    elif somme_total > nb_saisi :
        derniere_somme = i -1
        break
print(derniere_somme)


