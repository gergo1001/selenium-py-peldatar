def szokoev(evszam):
    vissza=False;
    if (evszam % 4 ==0):
        vissza=True;
    if (evszam%100==0 and evszam%400!=0):
        vissza=False
    return vissza

if (szokoev(int(input("Kérek egy évszámot: ")))):
    print("Szőkőév")
else:
    print("Nem szőkőév")