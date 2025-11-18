BASE = 4
fromage_base = 800.0
eau_base = 2.0
ail_base = 2.0
pain_base = 400.0

nbConvives = input("Entrez le nombre de personne(s) conviées à la fondue : ")

try:
    nbConvives = int(nbConvives)
except ValueError:
    print("Erreur : Veuillez entrer un nombre entier valide.")
    exit()

if BASE != 0:
    fromage_requis = fromage_base * nbConvives / BASE
    eau_requise = eau_base * nbConvives / BASE
    ail_requis = ail_base * nbConvives / BASE
    pain_requis = pain_base * nbConvives / BASE
else:
    print("Erreur : La base de la recette est nulle, impossible d'adapter les quantités.")
    exit()

print(f"\nPour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage_requis:.1f} gr de fromage")
print(f"- {eau_requise:.1f} dl d'eau")
print(f"- {ail_requis:.1f} gousse(s) d'ail")
print(f"- {pain_requis:.1f} gr de pain")
