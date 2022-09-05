import csv

with open('csv.csv', 'r') as csvFile: 
    csvReader = csv.reader(csvFile)
    for line in csvReader:
        print(line[3])