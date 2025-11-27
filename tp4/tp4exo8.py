etudiant = {
    'firstname': 'Atakan',
    'name': 'Gocer',
    'promo': 'RT',
    'group': '111'
}

etudiant2 = {
    'firstname': 'Charli',
    'name': 'Lechef',
    'promo': 'RT',
    'group': '112'
}

binome = {
    1 : etudiant,
    2 : etudiant2
}



print("Votre nom est", etudiant['name'],
      ", prénom est", etudiant['firstname'],
      ", vous faites partie de la promo", etudiant['promo'],
      "et votre groupe est", etudiant['group'])

print("Les clés du dictionnaire sont :")
for key in etudiant.keys():
    print("-", key)

print("Les valeurs du dictionnaire sont :")
for value in etudiant.values():
    print("-", value)

print("Les tuplets du dictionnaire sont :")
for item in etudiant.items():
    print("-", item)

print("Les étudiants formant le binôme sont :")
for personne in binome.values():
    print(f"- L'étudiant {personne['name']} {personne['firstname']} du groupe {personne['group']}")


