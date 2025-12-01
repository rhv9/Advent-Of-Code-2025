print("Hello WOrld!")

f = open("input/1.txt")
inputText = f.read()
inputList = inputText.splitlines()

dial:int = 50
result:int = 0

for line in inputList:
    count = 0
    if line[0] == 'R':
        num = int(line[1:])
        dial += num
        count = int(dial / 100)
        dial = dial % 100
    else :
        num = int(line[1:])
        prevDial = dial
        dial -= num
        if dial < 0 and prevDial != 0:
            count += 1
        count += abs(int(dial / 100))
        dial = dial % 100

    if dial == 0 and count > 0:
        count -= 1 
    if dial == 0:
        result += 1
    result += count

print("Result: ", result)
