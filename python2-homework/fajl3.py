with open('adat.txt', 'r') as f:
    my_list = f.readlines()

with open('masikfajl', 'w') as f2:
    for elem in my_list:
        f2.write(elem.replace('\n', ' '))