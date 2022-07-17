from operator import truediv


devideNum = int(input("please input the number you want your pairs to be devided by: "))
input = input("please input your list of numbers separated by commas: ")
input = input.replace(' ', '')
input = input.replace('[', '')
input = input.replace(']', '')
arrInput = input.split(',')
pairs = False
for i in range(0, len(arrInput)):
    for j in range(i+1, len(arrInput)):
        if (int(arrInput[i]) + int(arrInput[j])) % devideNum == 0:
            pairs = True
if pairs == True:
    print("pairs can be found")
else:
    print("pairs cannot be found")