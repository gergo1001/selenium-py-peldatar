with open('masik3.txt', 'w') as f2:
    f2.write("")
with open('adat.txt', 'r') as f:
    for line in f:
        with open('masik3.txt', 'a') as f2:
            f2.write(line)
