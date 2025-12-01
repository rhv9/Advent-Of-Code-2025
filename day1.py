print("Hello WOrld!")

f = open("input/1.txt")
inputText = f.read()
inputList = inputText.splitlines()

dial:int = 50
result:int = 0
for line in inputList:
    if line[0] == 'R':
        num = int(line[1:])
        dial += num
        dial = dial % 100
    else :
        num = int(line[1:])
        dial -= num
        dial = dial % 100

    if dial == 0:
        result += 1

print("Result: ", result)
