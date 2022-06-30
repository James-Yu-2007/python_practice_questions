input1 = input("please input your list of numbers separated by commas: ")
input1 = input1.replace(' ', '')
listInput = input1.split(',')
input2 = input("please input the number you want to check for: ")
numberExists = ()
for x in listInput:
    if x == input2:
        numberExists = True
if numberExists:
    print("your number exists in your list")
else:
    print("your number does not exist in your list")