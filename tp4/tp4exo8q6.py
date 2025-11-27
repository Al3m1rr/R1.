dic = {"name":"toto","firstname":"titi","promo":2022,"group":202}

print("Les clés du dictionnaire sont :")
for key in dic.keys():
    print("-", key)

print("Les valeurs du dictionnaire sont :")
for value in dic.values():
    print("-", value)

print("Les tuplets du dictionnaire sont :")
for item in dic.items():
    print("-", item)


