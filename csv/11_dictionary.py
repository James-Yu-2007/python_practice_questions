import csv

with open('csv.csv', 'r') as csvFile: 
    csvReader = csv.reader(csvFile)
    dictionary = {}
    list = []
    for line in csvReader:
        list.append(line)
dictionary['content' ] = list
print(dictionary)