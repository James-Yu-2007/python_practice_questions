input = input("please input the funciton you want defined: ")
input = input.replace(' ', '')
input = input.replace('(', '')
input = input.replace(')', '')

if input == "print":
    print("print(stuff) => stuff")
elif input == "abs":
    print("abs(number) => absolute value of number")
elif input == "round":
    print("round(4/3) => ")
else:
    print("this function is not in the dictionary")
    