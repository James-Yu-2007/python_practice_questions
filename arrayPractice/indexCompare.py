input = input("please input your array separated by commas: ")
input = input.replace(' ','')
input = input.replace('[','')
input = input.replace(']','')
arrInput = input.split(',')
numbers = []
for i in range(0, len(arrInput)):
    for j in range((i+1), len(arrInput)):
        if int(arrInput[j]) - int(arrInput[i]) > 0:
            numbers.append(int(j) - int(i))
print(max(numbers))
