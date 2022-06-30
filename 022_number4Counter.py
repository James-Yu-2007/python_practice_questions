input = input("please input your numers separated by commas: ")
input = input.replace(' ', '')
listInput = input.split(',')
numberOf4 = 0
for x in listInput:
    if x == "4":
        numberOf4 += 1
print("there are " + str(numberOf4) + " fours in your list of numbers")