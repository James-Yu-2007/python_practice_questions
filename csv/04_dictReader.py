import csv

data = csv.DictReader(open("csv.csv"))
for row in data:
   print(row)