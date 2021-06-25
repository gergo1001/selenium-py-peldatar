for i in range(5):
    szoveg=""
    for j in range(5):
        szoveg = szoveg + chr(97+i+(j*5))+" "+str(97+i+(j*5))+" "
    print(szoveg)
