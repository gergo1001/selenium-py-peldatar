import csv

with open('table_in.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    with open('table_out.txt', 'w', newline='') as outputfile:
        csvwriter = csv.writer(outputfile)
        for row in csvreader:
            csvwriter.writerow(row[:2])
