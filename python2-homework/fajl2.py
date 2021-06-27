with open('adat.txt', 'r') as f:
    my_list = f.read().splitlines()

for elem in my_list:
    print(elem, end=" ")
