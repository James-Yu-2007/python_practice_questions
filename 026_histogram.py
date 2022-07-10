input = input("please input your list of numbers separated by commas: ")
input = input.replace(' ', '')
listInput = input.split(',')
for n in listInput:
    output = ''
    times = n
    while( int(times) > 0 ):
        output += '*'
        times = int(times) - 1
    print(output)
