import csv

with open('csv.csv', newline='') as csvfile:
  data = csv.reader(csvfile, delimiter = '\t')
  for row in data:
    print(', '.join(row))