L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""


element_max = L1[0]
max_freq = 0

for elem in L1:
    freq = 0
    for x in L1:
        if x == elem:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        element_max = elem

print("Le nombre le plus frequent dans la liste est le :", element_max, "(", max_freq, "x)")






""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""