import csv

with open('csv.csv', 'r') as csvFile: 
    csvReader = csv.reader(csvFile, skipinitialspace = True)
    for line in csvReader:
        print(line)