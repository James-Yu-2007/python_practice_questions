strInput = input("please input your string: ")
intInput = int(input("please input the number of time you want you rstring to be duplicated: "))
if intInput > 0:
    if intInput < 2:
        while intInput > 0:
            print(strInput)
            intInput -= 1
    else:
        while intInput > 0:
            print(strInput[0:2])
            intInput -= 1
else:
    print("please input a positive integer")