nombre_demande = int(input(" Entrez un nombre entier : "))

if (nombre_demande %2 == 1) :
    if (nombre_demande > 0) :
        print("Le nombre est positif et impair")
    elif (nombre_demande < 0) :
        print("Le nombre est négatif et impair")

if (nombre_demande %2 == 0) :
    if (nombre_demande > 0) :
        print("Le nombre est positif et pair")
    elif (nombre_demande < 0) :
        print("Le nombre est négatif et pair")
    else :
        print("Le nombre est zéro (et il est pair)")



