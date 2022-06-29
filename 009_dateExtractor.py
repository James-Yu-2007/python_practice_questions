input = input("please input the month, the day, then the year in number form separated by a comma: ")
input = input.replace(' ', '')
listInput = input.split(',')
print(listInput[0] + " / " + listInput[1] + " / " + listInput[2])