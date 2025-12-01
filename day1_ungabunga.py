import time

f = open("input/1.txt")
inputText = f.read()
inputList = inputText.splitlines()

dial:int = 50
result:int = 0
start = time.time()
for line in inputList:
    sign = 1 if line[0] == 'R' else -1

    if line[0] == 'R':
        num = int(line[1:])
        for _ in range(0, num):
            dial += 1
            if dial > 99:
                dial = 0
            
    else:
        num = int(line[1:])
        for _ in range(0, num):
            dial -= 1
            if dial < 0:
                dial = 99

    if dial == 0:
        result += 1
end = time.time()

print("Result: ", result)
print((end - start) * 1000, "ms")
