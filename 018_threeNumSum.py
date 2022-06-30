input = input("please input your three numbers separated by commas: ")
input = input.replace(' ', '')
listInput = input.split(',')
if int(listInput[0]) == int(listInput[1]) == int(listInput[2]):
    print(9 * int(listInput[0]))
else:
    print(int(listInput[0]) + int(listInput[1]) + int(listInput[2]))