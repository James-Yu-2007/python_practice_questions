input = int(input("please input your number: "))
if abs(1000 - input < 100):
    print("true")
elif abs(2000 - input < 100):
    print("true")
else:
    print("false")