import csv

with open('titanic.csv', 'r') as csvFile: 
    csvReader = csv.reader(csvFile)
    age = []
    for row in csvReader:
        age.append(row[5])

list = age

for i in range(len(list)):
    for j in range(len(list)):
        if list[j] > list[i]:
            n = list[i]
            list[i] = list[j]
            list[j] = n
print(list)
