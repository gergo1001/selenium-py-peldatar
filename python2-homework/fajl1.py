with open('adat.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''), end=" ")
