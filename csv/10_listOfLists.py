import csv

with open('csv.csv', 'r') as csvFile: 
    csvReader = csv.reader(csvFile)
    list = []
    listOfList = []
    for line in csvReader:
        for i in line:
            print(i)
#             list.append(i)
#         listOfList.append(list)
# print(listOfList)