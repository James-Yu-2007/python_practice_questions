import calendar

input = ("please input the year and the month separated by a comma")
input = input.replace(' ', '')
listInput = input.split(',')
print(calendar.month(listInput[0], listInput[1]))