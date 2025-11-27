L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

element_max = L1[0]
max_freq = 0


for elem in L1:
    freq = L1.count(elem)
    if freq > max_freq:
        max_freq = freq
        element_max = elem

print("Le nombre le plus frequent dans la liste est le :", element_max, "(", max_freq, "x)")
