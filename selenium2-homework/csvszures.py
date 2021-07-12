import csv

csvfile = open('csv.csv', 'r');
csvoutput = open('csvoutput.csv', 'w', newline='');

spamwriter = csv.writer(csvoutput, delimiter=',')
csvreader = csv.reader(csvfile, delimiter=',')
for row in csvreader:
    spamwriter.writerow([row[1], row[0]])

csvfile.close();
csvoutput.close();
