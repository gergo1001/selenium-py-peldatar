osszszam=0
szam=int(input("Adjon meg egy egész számot: "))
osszszam+=szam
while szam<10:
    szam = int(input("adjon meg egy egész számot"))
    osszszam+=szam
print("megadott számok összege: ",osszszam)