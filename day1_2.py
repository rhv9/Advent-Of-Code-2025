import time


f = open("input/1.txt")
inputText = f.read()
inputList = inputText.splitlines()

dial:int = 50
result:int = 0

start = time.time()
for line in inputList:
    count = 0
    sign = 1 if line[0] == 'R' else -1
    num = int(line[1:])
    prevDial = dial
    dial += num * sign
    if sign == -1 and dial < 0 and prevDial != 0:
        count += 1

    count += abs(int(dial / 100))
    dial = dial % 100

    if dial == 0:
        result += 1
        # Remove extra count
        if (count > 0):
            count -= 1  

    result += count
end = time.time()

print("Result: ", result)
print((end - start) * 1000, "ms")
