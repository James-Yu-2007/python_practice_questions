import csv

with open('C:/Users/yujam/python_practice_questions/searchAndSorting/titanic.csv', 'r') as csvFile: 
    csvReader = csv.reader(csvFile)
    age = []
    next(csvReader)
    for row in csvReader:
        if row[5] != '':
            age.append(row)


list = age

for i in range(len(list)):
    for j in range(len(list)):
        if float(list[j][5]) > float(list[i][5]):
            tmp = list[i]
            list[i] = list[j]
            list[j] = tmp

with open('titanic.csv', 'w', newline='') as f:
    fieldNames = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
    thewriter = csv.DictWriter(f, fieldnames = fieldNames)
    for record in list:
        thewriter.writerow({'PassengerId' : record[0], 'Survived' : record[1], 'Pclass' : record[2], 'Name' : record[3], 'Sex' : record[4], 'Age' : record[5], 'SibSp' : record[6], 'Parch' : record[7], 'Ticket' : record[8], 'Fare' : record[9], 'Cabin' : record[10], 'Embarked' : record[11]})
