szamok = []
while True:
    szam = input("adj meg egy számot: ")
    szamok.append(szam)
    if szam == "0":
        break
for cv in range(len(szamok)):
    print(szamok[len(szamok) - (cv + 1)])
