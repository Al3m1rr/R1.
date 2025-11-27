liste = [5, 2, 4, 8, 1, 3]

print(liste)

N = len(liste)
for i in range(N):
    for j in range(i + 1, N):
        if liste[j] < liste[i]:
            liste[i], liste[j] = liste[j], liste[i]
    #print(liste)

#print(sorted(liste))
#liste.sort()
#print(liste)