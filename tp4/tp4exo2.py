nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))

moyenne = 0.0
notes = []


for i in range(nombreEtudiants):
    note = float(input("Note etudiant " + str(i) + " : "))




    while note < 0 or note > 20:
        print("Erreur : la note doit être comprise entre 0 et 20.")
        note = float(input("Note etudiant " + str(i) + " : "))

    notes.append(note)
    moyenne += note


moyenne = moyenne / nombreEtudiants


print("Moyenne de classe :", moyenne)
print("Numéro de l’Etudiant | note | ecart a la moyenne")

for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(i, "|", notes[i], "|", round(ecart, 2))


