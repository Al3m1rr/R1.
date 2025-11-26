import time


n = int(input("Entrez un nombre entier positif n: "))


if n <= 0:
    print("Le nombre doit être positif.")
else:

    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)



n = int(input("Entrez un nombre entier positif n: "))


if n <= 0:
    print("Le nombre doit être positif.")
else:

    while n >= 0:
        print(n)
        time.sleep(1)
        n -= 1
