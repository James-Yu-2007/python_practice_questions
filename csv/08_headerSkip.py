import csv

with open('csv.csv', 'r') as csvFile: 
    csvReader = csv.reader(csvFile)
    next(csvReader)
    for line in csvReader:
        print(line)