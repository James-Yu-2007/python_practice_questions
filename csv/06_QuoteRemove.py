import csv

with open('csv.csv', 'r') as csvFile: 
    csvReader = csv.reader(csvFile, skipinitialspace = True, quoting=csv.QUOTE_ALL)
    for line in csvReader:
        
        print(line)