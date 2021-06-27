szamok = []
while True:
    szam = input("adj meg egy számot: ")
    if szam == "0":
        break
    szamok.append(szam)

print(szamok[::-1])
